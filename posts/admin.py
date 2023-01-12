import mistune
from django.contrib import admin
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
from pygments.styles import get_style_by_name
from .models import Post


class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.rendered_content = markdown(obj.content)
        super().save_model(request, obj, form, change)


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if not info:
            return f"\n<pre><code>%s</code></pre>\n" % mistune.escape(code)
        lexer = get_lexer_by_name(info, stripall=True)
        formatter = html.HtmlFormatter(
            style=get_style_by_name("github-dark"),
            linenos="table",
            noclasses=True,
            wrapcode=True,
        )
        return highlight(code, lexer, formatter)


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


admin.site.register(Post, PostAdmin)
