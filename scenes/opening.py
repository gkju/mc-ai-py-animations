from manim import *


class TicTacToe(MobjectTable):
  board = []

  def __init__(self, moves):
    cross = VGroup(
      Line(UP + LEFT, DOWN + RIGHT),
      Line(UP + RIGHT, DOWN + LEFT),
    )
    b = cross.set_color(BLUE).scale(0.5)
    a = Circle().set_color(RED).scale(0.5)
    c = b.copy().set_color(BLACK)
    self.board = [[b.copy() if moves[i][j] == 1 else a.copy() if moves[i][j] == -1 else c.copy() for i in range(3)] for j in range(3)]
    super().__init__(self.board)

example_games = [
    [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
    ],
    [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0],
    ],
    [
      [-1, 0, 0],
      [0, 1, 0],
      [0, 0, 0],
    ],
    [
      [-1, 0, 0],
      [0, 1, 0],
      [0, 1, 0],
    ],
    [
      [-1, -1, 0],
      [0, 1, 0],
      [0, 1, 0],
    ],
    [
      [-1, -1, 1],
      [0, 1, 0],
      [0, 1, 0],
    ],
    [
      [-1, -1, 1],
      [0, 1, 0],
      [-1, 1, 0],
    ],
    [
      [-1, -1, 1],
      [1, 1, 0],
      [-1, 1, 0],
    ],
    [
      [-1, -1, 1],
      [1, 1, -1],
      [-1, 1, 0],
    ],
    [
      [-1, -1, 1],
      [1, 1, -1],
      [-1, 1, 1],
    ]
]

class OpeningManim(Scene):
  def construct(self):
    cur = TicTacToe(example_games[0])
    self.play(Write(cur))
    self.wait()
    for game in example_games[1:]:
      next = TicTacToe(game)
      self.play(ReplacementTransform(cur, next))
      cur = next
      self.wait()
    # self.play(cur.animate().scale(0.4).to_corner(UP + LEFT))
    matrix = Matrix(example_games[-1])
    self.play(ReplacementTransform(cur, matrix))
    self.wait(2)
    vertices = [1, 2, 3, 4, 5, 6, 7]
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    g = Graph(vertices, edges, layout="tree", layout_scale=3,
              vertex_config={
                7: {"fill_color": RED},
                6: {"fill_color": RED},
                4: {"fill_color": BLUE},
                5: {"fill_color": RED},
              }, root_vertex=1)
    self.play(matrix.animate().scale(0.4).to_edge(UP))
    self.wait(2)
    self.play(Write(g))
    self.wait(2)
    # scuffed, znalezc lepszy sposob (zwykle copy i zmiana nie da rady)
    b = Graph(vertices, edges, layout="tree", layout_scale=3,
              vertex_config={
      7: {"fill_color": RED},
      6: {"fill_color": RED},
      3: {"fill_color": BLUE},
      2: {"fill_color": BLUE},
      4: {"fill_color": BLUE},
      5: {"fill_color": RED},
    }, root_vertex=1)
    self.play(ReplacementTransform(g, b))
    self.wait(2)
    c = Graph(vertices, edges, layout="tree", layout_scale=3,
              vertex_config={
      7: {"fill_color": RED},
      6: {"fill_color": RED},
      3: {"fill_color": BLUE},
      2: {"fill_color": BLUE},
      4: {"fill_color": BLUE},
      5: {"fill_color": RED},
      1: {"fill_color": RED},
    }, root_vertex=1)
    self.play(ReplacementTransform(b, c))
    self.wait(2)
    self.play(FadeOut(c), FadeOut(matrix))
    self.wait(2)
    Theorem = VGroup(Tex(r"\textbf{Tw. (Zermelo): }"),
                     Tex(r"Kazda skonczona gra z doskonala informacja ma strategie wygrywajaca ("
                                             r"nieprzegrywajaca) dla jednego (obu) z graczy.")).arrange(DOWN)
    self.play(Write(Theorem))
    self.wait(2)