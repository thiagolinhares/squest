# Generated by Django 4.2.6 on 2023-11-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_catalog', '0034_alter_request_approval_workflow_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list'), 'ordering': ['-last_updated'], 'permissions': [('accept_request', 'Can accept request'), ('cancel_request', 'Can cancel request'), ('reject_request', 'Can reject request'), ('archive_request', 'Can archive request'), ('unarchive_request', 'Can unarchive request'), ('re_submit_request', 'Can re-submit request'), ('process_request', 'Can process request'), ('need_info_request', 'Can ask info request'), ('view_admin_survey', 'Can view admin survey'), ('list_approvers', 'Can view who can accept')]},
        ),
    ]