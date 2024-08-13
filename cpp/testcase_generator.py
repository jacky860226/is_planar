import random
import io
import os
import sys
import networkx as nx
from networkx.algorithms.planarity import check_planarity, is_planar
from networkx.classes.graph import Graph


def write_graph_to_TextIO(G: Graph, TextIO: io.TextIOBase):
    Index = 0
    mapping = {}
    nodes = list(G.nodes())
    random.shuffle(nodes)
    for node in nodes:
        mapping[node] = Index
        Index += 1
    TextIO.write(f"{Index} {len(G.edges())}\n")
    for u, v in G.edges():
        TextIO.write(f"{mapping[u]} {mapping[v]}\n")
    TextIO.flush()

def write_graph_to_file(G: Graph, file_name: str):
    with open(file_name, 'w') as f:
        write_graph_to_TextIO(G, f)

def print_graph(G: Graph):
    write_graph_to_TextIO(G, sys.stdout)

def get_golden_expected(G: Graph):
    if False:
        golden_expected, _ = check_planarity(G)
    else:
        golden_expected = is_planar(G)
    return golden_expected

def dump_case(G: Graph, expected: bool, case_index: int, dir = "."):
    if not os.path.exists(dir):
        os.makedirs(dir)
    write_graph_to_file(G, os.path.join(dir, str(case_index) + ".in"))
    golden_expected = get_golden_expected(G)
    assert golden_expected == expected
    with open(os.path.join(dir, str(case_index) + ".ans"), 'w') as f:
        f.write("YES\n" if expected else "NO\n")

case_index = 1
def generate_case(G: Graph, expected: bool, dir = "./data/secret"):
    global case_index
    dump_case(G, expected, case_index, dir)
    case_index += 1

class GenerateCases:
    def example_input_1(self):
        G = nx.Graph()
        G.add_edge(4, 6)
        G.add_edge(6, 3)
        G.add_edge(2, 0)
        G.add_edge(4, 0)
        G.add_edge(1, 3)
        G.add_edge(1, 0)
        G.add_edge(1, 5)
        G.add_edge(4, 5)
        G.add_edge(2, 3)
        G.add_edge(2, 5)
        expected = False
        generate_case(G, expected, "./data/sample")
    def generate_balanced_tree(self):
        expected = True
        generate_case(nx.balanced_tree(4, 4), expected)
    def generate_barbells(self):
        expected = True
        generate_case(nx.barbell_graph(4, 4), expected)
    def generate_circular_ladder(self):
        expected = True
        generate_case(nx.circular_ladder_graph(15), expected)
    def generate_cycle(self):
        expected = True
        generate_case(nx.cycle_graph(15), expected)
    def generate_dorogovtsev(self):
        expected = True
        generate_case(nx.dorogovtsev_goltsev_mendes_graph(7), expected)
    def generate_empty(self):
        expected = True
        generate_case(nx.empty_graph(15), expected)
    def generate_ladder(self):
        expected = True
        generate_case(nx.ladder_graph(5), expected)
    def generate_path(self):
        expected = True
        generate_case(nx.path_graph(100), expected)
    def generate_star(self):
        expected = True
        generate_case(nx.star_graph(100), expected)
    def generate_wheel(self):
        expected = True
        generate_case(nx.wheel_graph(100), expected)
    def generate_chvatal(self):
        expected = False
        generate_case(nx.chvatal_graph(), expected)
    def generate_cubical(self):
        expected = True
        generate_case(nx.cubical_graph(), expected)
    def generate_desargues(self):
        expected = False
        generate_case(nx.desargues_graph(), expected)
    def generate_diamond(self):
        expected = True
        generate_case(nx.diamond_graph(), expected)
    def generate_dodecahedral(self):
        expected = True
        generate_case(nx.dodecahedral_graph(), expected)
    def generate_frucht(self):
        expected = True
        generate_case(nx.frucht_graph(), expected)
    def generate_heawood(self):
        expected = False
        generate_case(nx.heawood_graph(), expected)
    def generate_house(self):
        expected = True
        generate_case(nx.house_graph(), expected)
    def generate_house_x(self):
        expected = True
        generate_case(nx.house_x_graph(), expected)
    def generate_icosahedral(self):
        expected = True
        generate_case(nx.icosahedral_graph(), expected)
    def generate_krackhardt_kite(self):
        expected = True
        generate_case(nx.krackhardt_kite_graph(), expected)
    def generate_moebius_kantor(self):
        expected = False
        generate_case(nx.moebius_kantor_graph(), expected)
    def generate_octahedral(self):
        expected = True
        generate_case(nx.octahedral_graph(), expected)
    def generate_pappus(self):
        expected = False
        generate_case(nx.pappus_graph(), expected)
    def generate_petersen(self):
        expected = False
        generate_case(nx.petersen_graph(), expected)
    def generate_sedgewick_maze(self):
        expected = True
        generate_case(nx.sedgewick_maze_graph(), expected)
    def generate_tetrahedral(self):
        expected = True
        generate_case(nx.tetrahedral_graph(), expected)
    def generate_truncated_cube(self):
        expected = True
        generate_case(nx.truncated_cube_graph(), expected)
    def generate_truncated_tetrahedron(self):
        expected = True
        generate_case(nx.truncated_tetrahedron_graph(), expected)
    def generate_tutte(self):
        expected = True
        generate_case(nx.tutte_graph(), expected)
    def generate_utility(self):
        expected = False
        generate_case(nx.LCF_graph(6, [3, -3], 3), expected)
    def generate_franklin(self):
        expected = False
        generate_case(nx.LCF_graph(12, [5, -5], 6), expected)
        generate_case(nx.LCF_graph(12, [-5, -3, 3, 5], 3), expected)
    def generate_mcgee(self):
        expected = False
        generate_case(nx.LCF_graph(24, [-12, 7, -7], 8), expected)
    def generate_levi(self):
        expected = False
        generate_case(nx.LCF_graph(30, [-13, -9, 7, -7, 9, 13], 5), expected)
    def generate_dyck(self):
        expected = False
        generate_case(nx.LCF_graph(32, [-13, 5, -5, 13], 8), expected)
    def generate_gray(self):
        expected = False
        generate_case(nx.LCF_graph(54, [-25, 7, -7, 13, -13, 25], 9), expected)
    def generate_balaban_10(self):
        expected = False
        generate_case(nx.LCF_graph(70, [68,-25,-18,29,13,35,-13,-29,19,25,9,-29,29,17,33,21,9,-13,-31,-9,25,17,9,-31,27,-9,17,-19,-29,27,-17,-9,-29,33,-25,25,-21,17,-17,29,35,-29,17,-17,21,-25,25,-33,29,9,17,-27,29,19,-17,9,-27,31,-9,-17,-25,9,31,13,-9,-21,-33,-17,-29,29], 1), expected)
    def generate_balaban_11(self):
        expected = False
        generate_case(nx.LCF_graph(112, [44,26,-47,-15,35,-39,11,-27,38,-37,43,14,28,51,-29,-16,41,-11,-26,15,22,-51,-35,36,52,-14,-33,-26,-46,52,26,16,43,33,-15,17,-53,23,-42,-35,-28,30,-22,45,-44,16,-38,-16,50,-55,20,28,-17,-43,47,34,-26,-41,11,-36,-23,-16,41,17,-51,26,-33,47,17,-11,-20,-30,21,29,36,-43,-52,10,39,-28,-17,-52,51,26,37,-17,10,-10,-45,-34,17,-26,27,-21,46,53,-10,29,-50,35,15,-47,-29,-41,26,33,55,-17,42,-26,-36,16], 1), expected)
    def generate_foster(self):
        expected = False
        generate_case(nx.LCF_graph(90, [17, -9, 37, -37, 9, -17], 15), expected)
    def generate_biggs_smith(self):
        expected = False
        generate_case(nx.LCF_graph(102, [16,24,-38,17,34,48,-19,41,-35,47,-20,34,-36,21,14,48,-16,-36,-43,28,-17,21,29,-43,46,-24,28,-38,-14,-50,-45,21,8,27,-21,20,-37,39,-34,-44,-8,38,-21,25,15,-34,18,-28,-41,36,8,-29,-21,-48,-28,-20,-47,14,-8,-15,-27,38,24,-48,-18,25,38,31,-25,24,-46,-14,28,11,21,35,-39,43,36,-38,14,50,43,36,-11,-36,-24,45,8,19,-25,38,20,-24,-14,-21,-8,44,-31,-38,-28,37], 1), expected)
    def generate_tutte_12_cage(self):
        expected = False
        generate_case(nx.LCF_graph(126, [17,27,-13,-59,-35,35,-11,13,-53,53,-27,21,57,11,-21,-57,59,-17], 7), expected)
    def generate_bidiakis_cube(self):
        expected = True
        generate_case(nx.LCF_graph(12, [6,4,-4], 4), expected)
    def generate_naruru(self):
        expected = False
        generate_case(nx.LCF_graph(24, [5,-9,7,-7,9,-5], 4), expected)
    def generate_f26a(self):
        expected = False
        generate_case(nx.LCF_graph(26, [-7,7], 13), expected)
    def generate_tutte_coxeter(self):
        expected = False
        generate_case(nx.LCF_graph(26, [-13,-9,7,-7,9,13], 5), expected)
    def generate_harries(self):
        expected = False
        generate_case(nx.LCF_graph(70, [-29,-19,-13,13,21,-27,27,33,-13,13,19,-21,-33,29], 5), expected)
    def generate_harries_wong(self):
        expected = False
        generate_case(nx.LCF_graph(70, [9,25,31,-17,17,33,9,-29,-15,-9,9,25,-25,29,17,-9,9,-27,35,-9,9,-17,21,27,-29,-9,-25,13,19,-9,-33,-17,19,-31,27,11,-25,29,-33,13,-13,21,-29,-21,25,9,-11,-19,29,9,-27,-19,-13,-35,-9,9,17,25,-9,9,27,-27,-21,15,-9,29,-29,33,-9,-25], 1), expected)
    def generate_Ljubljana(self):
        expected = False
        generate_case(nx.LCF_graph(26, [47,-23,-31,39,25,-21,-31,-41,25,15,29,-41,-19,15,-49,33,39,-35,-21,17,-33,49,41,31,-15,-29,41,31,-15,-25,21,31,-51,-25,23,9,-17,51,35,-29,21,-51,-39,33,-9,-51,51,-47,-33,19,51,-21,29,21,-31,-39], 2), expected)
    def generate_goldner_harary(self):
        """ from hagberg test_planarity_networkx.py """
        e = [(1,2), (1,3), (1,4), (1,5), (1,7), (1,8), (1,10),
             (1,11), (2,3), (2,4), (2,6), (2,7), (2,9), (2,10),
             (2,11), (3,4), (4,5), (4,6), (4,7), (5,7), (6,7),
             (7,8), (7,9), (7,10), (8,10), (9,10), (10,11)]
        expected = True
        generate_case(nx.Graph(e), expected)
    def generate_grid_2d_graph(self):
        def generate(n, m):
            g = nx.grid_2d_graph(n, m)
            expected = True
            generate_case(g, expected)
            g.add_edge((0,0), (n-1,m-1))
            generate_case(g, expected)
            expected = False
            node1, node2 = random.sample(list(g.nodes()), 2)
            g.add_edge(node1, node2)
            generate_case(g, expected)
        generate(1000, 100)
        generate(1000, 100)
        generate(100, 100)
        generate(100, 100)


def generateCases():
    global case_index
    cases = GenerateCases()
    cases.example_input_1()
    for method_name in dir(cases):
        if method_name.startswith("generate_"):
            print(method_name, case_index)
            method = getattr(cases, method_name)
            if callable(method):
                method()
    print("Number of case", case_index - 1)

random.seed(7122)
if __name__ == "__main__":
    generateCases()
