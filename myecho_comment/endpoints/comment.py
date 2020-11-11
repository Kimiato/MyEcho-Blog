from rest_framework.decorators import action
from rest_framework.views import Response
from rest_framework import status

from myecho.utils.rest_views import (
    BaseGenericViewSet,
    BaseListModelMixin,
    BaseDestroyModelMixin,
    BaseCreateModelMixin
)
from myecho.utils.toolfuns import _get_client_ip
from myecho.controllers.authentication import (
    BaseTokenAuthentication,
    action_authentication
)
from myecho.controllers.permissions import IsAdmin, action_permission
from myecho_comment.serializers import CommentSerializer
from myecho_comment.models import Comment


class CommentViewSet(BaseListModelMixin, BaseCreateModelMixin, BaseDestroyModelMixin, BaseGenericViewSet):
    """
        评论ViewSet
    """
    authentication_classes = []
    permission_classes = []
    queryset = Comment.objects.order_by('id')
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        """
            # 获取已审核的评论列表
        """
        self.queryset = self.queryset.filter(is_examine=True)
        return super(CommentViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            # 创建一条评论
        """
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        data = serializer.validated_data
        if self.request.user.is_authenticated:
            data.update({
                'user':self.request.user,
                'user_ip': _get_client_ip(self.request),
                'user_name': self.request.user.username,
                'user_email': self.request.user.email
            })
        else:
            data.update(user_ip=_get_client_ip(self.request))
        super(CommentViewSet, self).perform_create(serializer)


    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAdmin)
    def destroy(self, request, *args, **kwargs):
        """
            # 删除一条评论
        """
        return super(CommentViewSet, self).destroy(request, *args, **kwargs)

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAdmin)
    @action(methods=['PUT'], detail=True)
    def examine(self, request, pk):
        """
            # 审核评论(将评论状态修改为已审核)
        """
        instance = self.get_object()
        instance.is_examine = True
        instance.save()
        return Response({"details": "审核成功"}, status=status.HTTP_200_OK)

    @action_authentication(BaseTokenAuthentication)
    @action_permission(IsAdmin)
    @action(methods=['GET'], detail=True)
    def unexamined(self, request, pk, *args, **kwargs):
        """
            # 未审核的评论列表
        """
        self.queryset = self.queryset.filter(is_examine=False)
        return super(CommentViewSet, self).list(request, *args, **kwargs)
