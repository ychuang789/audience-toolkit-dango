from django import forms

from .models import LabelingJob, Label, UploadFileJob, Rule


class UploadFileJobForm(forms.ModelForm):
    class Meta:
        model = UploadFileJob
        fields = '__all__'
        exclude = ['labeling_job', 'job_status', 'created_by']
        widgets = {
            'file': forms.FileInput(attrs={'class': '.form-control-file.', }),
        }


class LabelingJobForm(forms.ModelForm):
    class Meta:
        model = LabelingJob
        fields = "__all__"
        exclude = ['created_by', 'is_multi_label']
        # last_job_id = 0  # LabelingJob.objects.last().id if LabelingJob.objects.last() is not None else 0
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'value': f'Jab'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'job_type': forms.Textarea(attrs={'class': 'form-control'}),
            'is_multi_label': forms.CheckboxInput(attrs={'class': 'custom-switch'}),
            'job_data_type': forms.Select(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'hidden': True})
        }


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ["labeling_job", "name", "description", "target_amount"]
        widgets = {
            'labeling_job': forms.Select(attrs={'class': 'form-control', 'disabled': False}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'hidden': True})
        }
        labels = {
            'name': '標籤名稱',
            'description': '描述與定義'
        }


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ["labeling_job", "name", "description"]
        exclude = ["target_amount"]
        widgets = {
            'labeling_job': forms.Select(attrs={'class': 'form-control', 'disabled': False}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'hidden': True})
        }
        labels = {
            'name': '標籤名稱',
            'description': '描述與定義'
        }


class RuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        label_id = kwargs.pop('label', None)
        super(RuleForm, self).__init__(*args, **kwargs)

        labeling_job_id = self.data.get('labeling_job', None)

        if label_id:
            self.fields['label'].queryset = Label.objects.filter(label_id=label_id)
        else:
            if labeling_job_id:
                self.fields['label'].queryset = Label.objects.filter(
                    labeling_job_id=labeling_job_id)

    class Meta:
        model = Rule
        fields = "__all__"
        exclude = ['created_at', 'created_by', 'rule_type']
        widgets = {
            'labeling_job': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'label': forms.Select(attrs={'class': 'form-control'}),
            'match_type': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class RegexForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'data' in kwargs:
            job_id = kwargs.get('data').get('labeling_job')
            label_id = kwargs.get('data').get('label')
        elif 'instance' in kwargs:
            instance = kwargs.get('instance')
            job_id = instance.labeling_job_id
            label_id = instance.label_id
        elif 'initial' in kwargs:
            instance = kwargs.get('initial')
            job_id = instance.get('labeling_job')
            label_id = instance.get('label')
        else:
            data = args[0]
            job_id = data.get('job', None) if 'job' in data else data.get('labeling_job', None)
            label_id = args[0].pop('label', None)
        super(RegexForm, self).__init__(*args, **kwargs)

        job_id = self.data.get('job_id', job_id)
        if label_id:
            self.fields['label'].initial = label_id
        if job_id:
            self.fields['label'].queryset = Label.objects.filter(
                labeling_job_id=job_id)
        else:
            self.fields['label'].queryset = self.instance.labeling_job.label_set.all()

    class Meta:
        model = Rule
        fields = "__all__"
        exclude = ['created_at', 'created_by', 'match_type', 'score', 'rule_type']
        widgets = {
            'labeling_job': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'label': forms.Select(attrs={'class': 'form-control'}),
        }


class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        if self.instance.labeling_job_id:
            self.fields['labels'].queryset = Label.objects.filter(
                job_id=self.instance.labeling_job_id)
