from django.urls import path
from tasks.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TagUpdateView,
    TaskDeleteView,
    TagDeleteView,
    toggle_task_status,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("add_task/", TaskCreateView.as_view(), name="add_task"),
    path("add_tag/", TagCreateView.as_view(), name="add_tag"),
    path(
        "update_task/<int:pk>/",
        TaskUpdateView.as_view(),
        name="update_task"
    ),
    path(
        "delete_task/<int:pk>/",
        TaskDeleteView.as_view(),
        name="delete_task"
    ),
    path("update_tag/<int:pk>/", TagUpdateView.as_view(), name="update_tag"),
    path("delete_tag/<int:pk>/", TagDeleteView.as_view(), name="delete_tag"),
    path(
        "toggle_task_status/<int:task_id>/",
        toggle_task_status,
        name="toggle_task_status",
    ),
]
