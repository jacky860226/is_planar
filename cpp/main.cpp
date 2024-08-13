#include <bits/stdc++.h>
using namespace std;
struct FringeOpposedSubset {
  deque<int> left, right;
  FringeOpposedSubset(int h) : left{h}, right() {}
};
struct Fringe {
  deque<FringeOpposedSubset> FOPs;
  Fringe(int h) : FOPs{{h}} {}
  bool operator<(const Fringe& other) const {
    auto diff = FOPs.back().left.back() - other.FOPs.back().left.back();
    if (diff != 0) return diff < 0;
    return FOPs.front().left.front() < other.FOPs.front().left.front();
  }
  void merge(Fringe& other) {
    other.merge_t_alike_edges();
    merge_t_opposite_edges_into(other);
    if (FOPs.front().right.empty())
      other.align_duplicates(FOPs.back().left.front());
    else
      make_onion_structure(other);
    if (other.FOPs.front().left.size()) FOPs.push_front(other.FOPs.front());
  }
  void merge_t_alike_edges() {
    if (!FOPs.front().right.empty()) throw runtime_error("Exception");
    for (auto it = next(FOPs.begin()); it != FOPs.end(); ++it) {
      if (!it->right.empty()) throw runtime_error("Exception");
      FOPs.front().left.insert(
          FOPs.front().left.end(), it->left.begin(), it->left.end());
    }
    FOPs = decltype(FOPs){FOPs.front()};
  }
  void merge_t_opposite_edges_into(Fringe& other) {
    while (FOPs.front().right.empty() &&
           FOPs.front().left.front() > other.FOPs.front().left.back()) {
      other.FOPs.front().right.insert(
          other.FOPs.front().right.end(), FOPs.front().left.begin(),
          FOPs.front().left.end());
      FOPs.pop_front();
    }
  }
  void align_duplicates(int dfs_h) {
    if (FOPs.front().left.back() == dfs_h) {
      FOPs.front().left.pop_back();
      swap_side();
    }
  }
  void swap_side() {
    if (FOPs.front().left.empty() ||
        (!FOPs.front().right.empty() &&
         FOPs.front().left.back() > FOPs.front().right.back())) {
      swap(FOPs.front().left, FOPs.front().right);
    }
  }
  void make_onion_structure(Fringe& other) {
    auto low = &FOPs.front().left, high = &FOPs.front().right;
    if (FOPs.front().left.front() >= FOPs.front().right.front())
      swap(low, high);
    if (other.FOPs.front().left.back() < low->front())
      throw runtime_error("Exception");
    if (other.FOPs.front().left.back() < high->front()) {
      low->insert(
          low->begin(), other.FOPs.front().left.rbegin(),
          other.FOPs.front().left.rend());
      high->insert(
          high->begin(), other.FOPs.front().right.rbegin(),
          other.FOPs.front().right.rend());
      other.FOPs.front().left.clear();
      other.FOPs.front().right.clear();
    }
  }
  auto lr_condition(int dfs_height) const {
    bool left_condition =
        !FOPs.front().left.empty() && FOPs.front().left.front() >= dfs_height;
    bool right_condition =
        !FOPs.front().right.empty() && FOPs.front().right.front() >= dfs_height;
    return make_pair(left_condition, right_condition);
  }
  void prune(int dfs_height) {
    auto [left, right] = lr_condition(dfs_height);
    while (!FOPs.empty() && (left || right)) {
      if (left) FOPs.front().left.pop_front();
      if (right) FOPs.front().right.pop_front();
      if (FOPs.front().left.empty() && FOPs.front().right.empty())
        FOPs.pop_front();
      else
        swap_side();
      if (!FOPs.empty()) tie(left, right) = lr_condition(dfs_height);
    }
  }
};
unique_ptr<Fringe> get_merged_fringe(deque<unique_ptr<Fringe>>& upper) {
  if (upper.empty()) return nullptr;
  sort(upper.begin(), upper.end(), [](auto& a, auto& b) { return *a < *b; });
  auto new_fringe = move(upper[0]);
  for (auto it = next(upper.begin()); it != upper.end(); ++it)
    new_fringe->merge(**it);
  return new_fringe;
}
void merge_fringes(vector<deque<unique_ptr<Fringe>>>& fringes, int dfs_height) {
  auto mf = get_merged_fringe(fringes.back());
  fringes.pop_back();
  if (mf) {
    mf->prune(dfs_height);
    if (mf->FOPs.size()) fringes.back().push_back(move(mf));
  }
}
struct Edge {
  int from, to;
  Edge(int from, int to) : from(from), to(to) {}
  bool operator==(const Edge& other) const {
    return from == other.from && to == other.to;
  }
};
struct Graph {
  int n = 0;
  vector<vector<int>> neighbor;
  vector<Edge> edges;
  void add_edge(int from, int to) {
    if (from == to) return;
    edges.emplace_back(from, to);
    edges.emplace_back(to, from);
  }
  void build() {
    sort(edges.begin(), edges.end(), [](const auto& a, const auto& b) {
      return a.from < b.from || (a.from == b.from && a.to < b.to);
    });
    edges.erase(unique(edges.begin(), edges.end()), edges.end());
    n = 0;
    for (auto& e : edges) n = max(n, max(e.from, e.to) + 1);
    neighbor.resize(n);
    for (auto& e : edges) neighbor[e.from].push_back(e.to);
  }
};

Graph g;
vector<int> dfs_heights;
vector<deque<unique_ptr<Fringe>>> fringes;

//*
bool dfs(int x, int parent = -1) {
  for (int y : g.neighbor[x]) {
    if (y == parent) continue;
    if (dfs_heights[y] < 0) {  // tree edge
      fringes.push_back({});
      dfs_heights[y] = dfs_heights[x] + 1;
      if (!dfs(y, x)) return false;
    } else if (dfs_heights[x] > dfs_heights[y]) {  // back edge
      fringes.back().push_back(make_unique<Fringe>(dfs_heights[y]));
    }
  }
  try {
    if (fringes.size() > 1) merge_fringes(fringes, dfs_heights[parent]);
  } catch (const exception& e) {
    return false;
  }
  return true;
}
/*/
bool dfs(int root) {
  std::stack<std::tuple<int, int, int>> dfs_stack;
  dfs_stack.push({root, -1, -1});
  while (dfs_stack.size()) {
    auto& [x, yID, parent] = dfs_stack.top();
    ++yID;
    if (yID == g.neighbor[x].size()) {
      dfs_stack.pop();
      try {
        if (fringes.size() > 1) merge_fringes(fringes, dfs_heights[parent]);
      } catch (const std::exception& e) {
        return false;
      }
    } else {
      auto y = g.neighbor[x][yID];
      if (y == parent) continue;
      if (dfs_heights[y] < 0) {  // tree edge
        fringes.push_back({});
        dfs_heights[y] = dfs_heights[x] + 1;
        dfs_stack.push({y, -1, x});
      } else if (dfs_heights[x] > dfs_heights[y]) {  // back edge
        fringes.back().push_back(make_unique<Fringe>(dfs_heights[y]));
      }
    }
  }
  return true;
}
//*/
bool is_planar() {
  dfs_heights.assign(g.n, -1);
  for (int i = 0; i < g.n; ++i) {
    fringes.clear();
    dfs_heights[i] = 0;
    if (!dfs(i)) return false;
  }
  return true;
}
int main() {
  int n, m, u, v;
  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    cin >> u >> v;
    g.add_edge(u, v);
  }
  g.build();
  cout << (is_planar() ? "YES" : "NO") << endl;
  return 0;
}