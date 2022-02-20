from typing import List, NamedTuple, Any
import pickle
import pathlib
import docutils.nodes
import logging
import pathlib
import pydear.imgui as ImGui

HERE = pathlib.Path(__file__).absolute().parent
ENV = HERE.parent / 'build/.doctrees/environment.pickle'

logger = logging.getLogger(__name__)

FONT_PATH = 'C:/Windows/Fonts/msgothic.ttc'


class DocTree(NamedTuple):
    docname: str
    path: pathlib.Path
    data: Any


def show_doctree(node: docutils.nodes.Node, path):
    flags = 0
    if not node.children:
        flags |= ImGui.ImGuiTreeNodeFlags_.Leaf
        flags |= ImGui.ImGuiTreeNodeFlags_.Bullet
    if ImGui.TreeNodeEx(f'{node.tagname}###{path}', flags):
        for i, child in enumerate(node.children):
            show_doctree(child, path + (i,))
        ImGui.TreePop()


def main():
    import sphinx.environment
    env: sphinx.environment.BuildEnvironment = pickle.loads(ENV.read_bytes())

    logging.basicConfig(level=logging.DEBUG)

    from pydear.utils import glfw_app
    app = glfw_app.GlfwApp('env_view')

    SELECTED: List[DocTree] = [DocTree('', pathlib.Path(''), None)]

    def draw(p_open):
        if ImGui.Begin('env', p_open):
            selected = None
            for docname, mtime in env.all_docs.items():
                if ImGui.Selectable(docname, docname == SELECTED[0].docname):
                    selected = docname

            if selected:
                path = pathlib.Path(env.doctreedir) / f'{selected}.doctree'
                if path.exists():
                    import pickle
                    SELECTED[0] = DocTree(
                        selected, path, pickle.loads(path.read_bytes()))

        ImGui.End()

    def show_selected(p_open):
        if ImGui.Begin('selected', p_open):

            if SELECTED[0]:
                dt = SELECTED[0]
                if dt.data:
                    show_doctree(dt.data, ())

        ImGui.End()

    from pydear.utils.dockspace import Dock, DockingGui

    class Gui(DockingGui):
        def _setup_font(self):
            io = ImGui.GetIO()
            io.Fonts.AddFontFromFileTTF(
                FONT_PATH, 24, None, io.Fonts.GetGlyphRangesJapanese())
            io.Fonts.Build()
    views = [
        Dock('env', draw),
        Dock('selected', show_selected),
    ]
    gui = Gui(app.loop, docks=views)

    from pydear.backends.impl_glfw import ImplGlfwInput
    impl_glfw = ImplGlfwInput(app.window)
    while app.clear():
        impl_glfw.process_inputs()
        gui.render()


if __name__ == '__main__':
    main()
