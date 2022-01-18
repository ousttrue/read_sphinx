import pickle
import pathlib
import sphinx.environment
import logging
import pathlib
import ctypes
import glfw
from OpenGL import GL
import pydear as ImGui
from pydear.utils.dockspace import dockspace, DockView

HERE = pathlib.Path(__file__).absolute().parent
ENV = HERE.parent / 'build/.doctrees/environment.pickle'

logger = logging.getLogger(__name__)

# Dear ImGui: standalone example application for GLFW + OpenGL 3, using programmable pipeline
# (GLFW is a cross-platform general purpose library for handling windows, inputs, OpenGL/Vulkan/Metal graphics context creation, etc.)
# If you are new to Dear ImGui, read documentation from the docs/ folder + read the top of ImGui.cpp.
# Read online: https://github.com/ocornut/imgui/tree/master/docs


def glfw_error_callback(error: int, description: str):
    logger.error(f"Glfw Error {error}: {description}")


class ImGuiApp:
    def __init__(self, window: glfw._GLFWwindow) -> None:
        self.window = window

        # Setup Dear ImGui context
        # IMGUI_CHECKVERSION()
        ImGui.CreateContext()
        io = ImGui.GetIO()
        # create texture before: ImGui.NewFrame()
        # io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;     // Enable Keyboard Controls
        # io.ConfigFlags |= ImGuiConfigFlags_NavEnableGamepad;      // Enable Gamepad Controls
        io.ConfigFlags |= ImGui.ImGuiConfigFlags_.DockingEnable  # before load ini

        # Setup Dear ImGui style
        # ImGui.StyleColorsDark()
        # ImGui.StyleColorsClassic();

        font_size = 20.0

        from pydear.utils import fontloader
        fontloader.load(pathlib.Path("C:/Windows/Fonts/MSGothic.ttc"), font_size,
                        io.Fonts.GetGlyphRangesJapanese())

        import fontawesome47
        icons_ranges = (ctypes.c_ushort * 3)(0xf000, 0xf3ff, 0)
        fontloader.load(fontawesome47.get_path(), font_size, icons_ranges,
                        merge=True, monospace=True)

        io.Fonts.Build()

        # Setup Platform/Renderer backends
        # ImGui_ImplGlfw_InitForOpenGL(window, True)
        # ImGui_ImplOpenGL3_Init(glsl_version)
        from pydear.backends.glfw import GlfwRenderer
        self.impl_glfw = GlfwRenderer(window)
        from pydear.backends.opengl import Renderer
        self.impl_opengl = Renderer()

        # Our state
        self.clear_color = (ctypes.c_float * 4)(0.45, 0.55, 0.60, 1.00)

        # 5.
        from pydear.utils.loghandler import ImGuiLogHandler
        log_handler = ImGuiLogHandler()
        log_handler.setFormatter(logging.Formatter(
            '%(name)s:%(lineno)s[%(levelname)s]%(message)s'))
        log_handler.register_root()
        log = DockView('log', (ctypes.c_bool * 1)(True), log_handler.draw)

        self.views = [
            log
        ]

    def __del__(self):
        del self.impl_opengl
        del self.impl_glfw
        ImGui.DestroyContext()

    def menu(self):
        if ImGui.BeginMenu(b"File", True):
            if ImGui.MenuItem(b"Quit", None, False, True):
                glfw.set_window_should_close(self.window, True)
            ImGui.EndMenu()

    def update(self):
        self.impl_glfw.process_inputs()
        # update ImGui
        ImGui.NewFrame()
        dockspace(self.views, menu=self.menu)
        ImGui.Render()

    def render(self):
        self.impl_opengl.render(ImGui.GetDrawData())


class GlfwApp:
    def __init__(self, width: int = 1280, height: int = 720) -> None:
        # Setup window
        glfw.set_error_callback(glfw_error_callback)
        if not glfw.init():
            raise RuntimeError('fail to glfw.init')

        # GL 3.0 + GLSL 130
        # glsl_version = "#version 130"
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
        glfw.window_hint(glfw.OPENGL_PROFILE,
                         glfw.OPENGL_CORE_PROFILE)  # 3.2+ only

        # Create window with graphics context
        self.window = glfw.create_window(
            width, height, "EnvironmentViewer", None, None)
        if not self.window:
            raise RuntimeError('fail to glfw.create_window')

        glfw.make_context_current(self.window)
        glfw.swap_interval(1)  # Enable vsync

    def __del__(self):
        glfw.destroy_window(self.window)
        glfw.terminate()

    def begin_frame(self) -> bool:
        if glfw.window_should_close(self.window):
            return False
        glfw.poll_events()
        return True

    def end_frame(self):
        glfw.swap_buffers(self.window)


def main():
    env: sphinx.environment.BuildEnvironment = pickle.loads(ENV.read_bytes())

    logging.basicConfig(level=logging.DEBUG)

    app = GlfwApp()
    gui = ImGuiApp(app.window)

    def draw(p_open):
        if ImGui.Begin('env'):
            for docname, mtime in env.all_docs.items():
                ImGui.Selectable(docname)
            pass
        ImGui.End()

    gui.views.append(
        DockView('env', None, draw)
    )

    while app.begin_frame():

        gui.update()

        # clear OpenGL
        display_w, display_h = glfw.get_framebuffer_size(app.window)
        GL.glViewport(0, 0, display_w, display_h)
        GL.glScissor(0, 0, display_w, display_h)
        GL.glClearColor(gui.clear_color[0] * gui.clear_color[3],
                        gui.clear_color[1] * gui.clear_color[3],
                        gui.clear_color[2] * gui.clear_color[3],
                        gui.clear_color[3])
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        # render ImGui
        gui.render()
        app.end_frame()
    del gui


if __name__ == '__main__':
    main()
