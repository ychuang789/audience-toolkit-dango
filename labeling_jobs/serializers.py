from rest_framework import serializers

from labeling_jobs.models import LabelingJob, Label


class LabelingJobSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="labeling_jobs:labelingjob-detail")
    created_by = serializers.StringRelatedField()

    class Meta:
        model = LabelingJob
        fields = "__all__"
        # fields = ["id", "name", "description", "is_multi_label",
        #           "job_data_type", "created_at", "updated_at", "created_by"]


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    # show
    id = serializers.IntegerField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="labeling_jobs:label-detail")
    # 傳三個引數
    # view_name='test':路由名字,用來反向解析
    # lookup_field='publish_id':要反向解析的引數值
    # lookup_url_kwarg='id':有名分組的名字
    # labeling_job = serializers.HyperlinkedIdentityField(
    #     view_name="labeling_jobs:job-detail",
    #     lookup_field='labeling_job_id',
    #     lookup_url_kwarg="pk",
    # )
    job = serializers.StringRelatedField()

    # job_id用來指定對應到的job
    job_id = serializers.IntegerField(label="Job ID", required=True)

    class Meta:
        model = Label
        fields = "__all__"
        # exclude = ["job"]
        # fields = ["id", "job", "name", "description", "target_amount", "job_id"]

