from django.contrib import admin
from django.utils.html import format_html
from .models import Process


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('user', 'process_time_sec', 'created_at', 'status', 'progress_bar')
    readonly_fields = ('started_at',)
    list_filter    = ('status', 'created_at', )

    def progress_bar(self, obj):
        if obj.status == Process.PENDING:
            return format_html('''<progress value="0" max="100"></progress>
                                <span style="font-weight:bold">0%</span>''')
        elif obj.status == Process.STARTED:
            return format_html('''<progress value="30" max="100"></progress>
                                <span style="font-weight:bold">30%</span>''')
        elif obj.status == Process.FINISHED:
            return format_html('''<progress value="100" max="100"></progress>
                                <span style="font-weight:bold">100%</span>''')
