import wtforms


class TinyMce(object):
    """
    Automatically makes TextProperty fields into TinyMCE editors (for the admin interface
    or any templates that include the tinymce macros).

    You can specify that it should only work for certain flelds by setting Controller.Meta.tinymce_fields.
    """

    def __init__(self, controller):
        self.controller = controller
        self.controller.events.before_render += self.before_render
        self.controller.meta.view.events.layout_scripts += self.layout_scripts

    def get_fields(self):
        if not hasattr(self.controller.meta, 'tinymce_fields'):
            return None
        return self.controller.meta.tinymce_fields

    def before_render(self, controller, *args, **kwargs):
        form = controller.context.get('form', None)
        if form and isinstance(form, (wtforms.Form)):
            fields = self.get_fields() or (field for field in form)
            for field in fields:
                if isinstance(field, wtforms.fields.simple.TextAreaField):
                    field.flags.tinymce = True

    def layout_scripts(self):
        return """
<script type="text/javascript" src="/plugins/tiny_mce/tinymce/jquery.tinymce.min.js"></script>
<script type="text/javascript" src="/plugins/tiny_mce/media_picker.js"></script>
<script type="text/javascript" src="/plugins/tiny_mce/embed.js"></script>
"""
