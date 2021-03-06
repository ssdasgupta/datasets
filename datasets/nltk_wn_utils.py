from typing import List, Callable, Mapping, Any, Tuple, Optional
from nltk.corpus import wordnet as wn
import networkx as nx
from nltk.corpus.reader.wordnet import Synset
import logging
logger = logging.getLogger(__name__)


def get_graph(start: Synset, relation: Callable[[Synset], List[Synset]]):
    """ Get the graph in the form of recurssive lists formed by doing
    depth-first walk starting from start and following edges relation"""

    return start.tree(relation)


def add(self_node: Synset,
        parent_list: List[Synset],
        g: nx.DiGraph,
        parent: bool = True):

    for n in parent_list:
        g.add_node(n[0].name())

        if parent:
            g.add_edge(self_node.name(), n[0].name())
        else:
            g.add_edge(n[0].name(), self_node.name())

    return g


def add_recurse(node_list: List, g: nx.DiGraph, parent: bool = True):
    """Works on the output generated by get_graph.

        Set parent=False if you want to reverse the edges
    """

    if len(node_list) > 1:
        add(node_list[0], node_list[1:], g, parent=parent)

        for parent in node_list[1:]:
            add_recurse(parent, g, parent=parent)

    return g


def get_nx_graph(start: Synset,
                 relation: Callable[[Synset], List[Synset]],
                 parent: bool = True) -> nx.DiGraph:
    wn_graph = get_graph(start, relation)
    nx_graph = nx.DiGraph()
    nx_graph = add_recurse(wn_graph, nx_graph, parent=parent)

    return nx_graph


def draw_to_file(graph: nx.DiGraph, filename: str) -> None:
    a_graph = nx.nx_agraph.to_agraph(graph)
    a_graph.layout('dot')
    a_graph.draw('filename')


def create_triples(graph: nx.DiGraph,
                   node2int: Optional[Mapping] = None,
                   relation: Any = 0,
                   create_int_ids: bool = False
                   ) -> Tuple[List[Tuple[Any, Any, Any]], Mapping]:

    if node2int is None and create_int_ids:
        node2int = create_unique_int_ids(graph)

    if node2int is None:
        node2int = {}

        def n2i(n):
            node2int[n] = n

            return n
    else:

        def n2i(n):
            return node2int[n]

    samples = [(n2i(head), n2i(tail), relation)
               for head, tail in graph.edges()]

    return samples, node2int


def create_unique_int_ids(graph: nx.DiGraph) -> Mapping[str, int]:
    n2i = {}
    i = 0

    for node in graph.nodes():
        if node in n2i:
            logger.warn("{} already present. Assigning same index")
        else:
            n2i[node] = i
            i += 1

    return n2i
