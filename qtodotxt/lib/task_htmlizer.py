class TaskHtmlizer(object):
    def __init__(self):
        self.priority_colors = dict(
            A='red',
            B='green',
            C='cyan')
    
    def task2html(self, task):
        text = task.text
        for context in task.contexts:
            text = text.replace('@' + context, self._htmlizeContext(context))
        for project in task.projects:
            text = text.replace('+' + project, self._htmlizeProject(project))
        if task.priority is not None:
            text = text.replace('(%s)' % task.priority, self._htmlizePriority(task.priority))
        return text
    
    def _htmlizeContext(self, context):
        return '<b><font color="green">@%s</font></b>' % context

    def _htmlizeProject(self, project):
        return '<b><font color="blue">+%s</font></b>' % project
    
    def _htmlizePriority(self, priority):
        if priority in self.priority_colors:
            color = self.priority_colors[priority]
            return '<b><font color="%s">(%s)</font></b>' % (color, priority)
        return '<b>(%s)</b>' % priority
