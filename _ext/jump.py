from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.locale import _


class jump(nodes.Admonition, nodes.Element):
    pass

def visit_jump_node(self, node):
    self.visit_admonition(node)

def depart_jump_node(self, node):
    self.depart_admonition(node)

class JumpDirective(Directive):

    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = "jump-%d" % env.new_serialno('jump')
        targetnode = nodes.target('', '', ids=[targetid])

        jump_node = jump('\n'.join(self.content))
        jump_node += nodes.title(_('Jump'), _('Jump'))
        self.state.nested_parse(self.content, self.content_offset, jump_node)

        if not hasattr(env, 'jump_all_jumps'):
            env.jump_all_jumps = []
        env.jump_all_jumps.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'jump': jump_node.deepcopy(),
            'taget': targetnode,
        })

        return [targetnode, jump_node]



def setup(app):
    app.add_config_value('jump_include_jumps', False, 'html')

    app.add_node(jump,
                 html=(visit_jump_node, depart_jump_node),
                 latex=(visit_jump_node, depart_jump_node),
                 text=(visit_jump_node, depart_jump_node))

    app.add_directive('jump', JumpDirective)

    return{'version': '0.1'}
