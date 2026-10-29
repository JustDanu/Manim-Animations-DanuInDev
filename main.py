from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        dots = [Dot().set_color(WHITE) for i in range(12)]
        grid = VGroup(*dots)

        grid.arrange_in_grid(rows=3, cols=4, buff=0.5)

        self.play(FadeIn(grid, lag_ratio=0.1))
        self.wait()

        target_dot = grid[6]
        self.play(target_dot.animate.scale(1.5).set_fill(YELLOW_A, opacity=1), Indicate(target_dot, color=YELLOW_A))
        self.wait()

