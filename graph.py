class graph(vertex):

	def __init__(self):
		self.vertexs = set()

	def add_vertex(self, vertex):
		self.vertexs.add(vertex)

	def remove_vertex(self, vertex):
		for v in vertex.successores:
			vertex.remove_successor(v)
		for v in vertex.predecessores:
			vertex.remove_successor(v)
		vertex.remove_vertex()

	def connect(self, vertex1, vertex2):
		vertex1.add_successor(vertex2)
		vertex2.add_predecessor(vertex1)

	def disconnect(self, vertex1, vertex2):
		vertex1.remove_successor(vertex2)
		vertex2.remove_predecessor(vertex1)

	def order(self):
		return len(vertexs)

	def vertex(self):
		return self.vertexs

	def one_vertice(self):
		vertex = self.vertexs.pop()
		self.vertexs.add(vertex)
		return vertex

	def adjacent(self, vertex):
		conj = set()
		conj.append(vertex.successores)
		for v in vertexs:
			if vertex in v.predecessores:
				conj.add(v)
		return conj

	def grade(self, vertex):
		return len(self.adjacent(vertex))

	def is_regular(self):
		n = self.grau(self.one_vertex())
		for v in vertexs:
			if self.grau(v) not in n:
				return False
		return True

	def is_complete(self):
		n = self.order - 1
		for v in self.vertex:
			if self.grade(v) not in n:
				return False
		return True

	def transitive_closure(self, vertex):
		group = {}
		return self.search_transitive_closure(vertex, group)

	def search_transitive_closure(self, vertex, visited):
		visited.append(vertex)
		for adj in self.adjacent(vertex)
			if adj not in visited:
				self.search_transitive_closure(adj, visited)
		return visited


	def is_connected(self):
		return self.vertexs.equals(self.transitive_closure(self.one_vertex()))

	def is_tree(self):
		v = self.one_vertex()
		group = {}
		return self.is_connected and not self.is_cycle(v, v, group)

	def is_cycle(self, vertex, previous, visited):
		if vertex in visited:
			return True
		visited.append(v)
		for adj in self.adjacent(vertex):
			if adj not in previus:
				if is_cycle(adj, v, visited)
					return True
		visited.remove_vertex(vertex)
		return False


	def topological_ordering(self):
		ordination = []
		group = {}
		for v in self.vertexs:
			if not self.v.predecessores:
				group.append(v)
		while group:
			v = group.pop()
			ordination.append(v)
			for m in v.successores:
				self.disconnect(v, m)
				if not m.predecessores:
					group.append(m)
		return ordination

	def planning(self):
		charge = 30
		plan = []
		semester = {}
		ordination = topological_ordering()
		for v in ordination:
			if not v.studied and charge != 0:
				plan.append(v)
				charge-= v.credits
				v.studied = True
		semester.append(plan)
		charge = 30
		plan = []
		return semester

class vertex():

	def __init__(self, code, credits = None):
		self.code = code
		self.credits = credits
		self.studied = False
		self.successores = set()
		self.predecessores = set()

	def add_successor(self, vertex):
		self.successores.add(vertex)

	def remove_successor(self, vertex):
		self.successores.remove(vertex)

	def add_predecessor(self, vertex):
		self.predecessores.add(vertex)

	def remove_predecessor(self, vertex):
		self.predecessores.remove(vertex)]

	def main():
		gnew = graph()

		INE5402 = vertex("INE5402",6)
		MTM5161 = vertex("MTM5161",4)
		INE5403 = vertex("INE5403",6)
		EEL5105 = vertex("EEL5105",5)
		INE5401 = vertex("INE5401",2)

		INE5404 = vertex("INE5404",6)
		MTM7174 = vertex("MTM7174",4)
		INE5405 = vertex("INE5405",5)
		MTM5512 = vertex("MTM5512",4)
		INE5406 = vertex("INE5406",5)
		INE5407 = vertex("INE5407",3)

		INE5408 = vertex("INE5408",6)
		INE5410 = vertex("INE5410",4)
		INE5409 = vertex("INE5409",4)
		MTM5245 = vertex("MTM5245",4)
		INE5411 = vertex("INE5411",6)

		INE5417 = vertex("INE5417",5)
		INE5413 = vertex("INE5413",4)
		INE5415 = vertex("INE5415",4)
		INE5416 = vertex("INE5416",5)
		INE5412 = vertex("INE5412",4)
		INE5414 = vertex("INE5414",4)

		INE5419 = vertex("INE5419",4)
		INE5423 = vertex("INE5423",4)
		INE5420 = vertex("INE5420",4)
		INE5421 = vertex("INE5421",4)
		INE5418 = vertex("INE5418",4)
		INE5422 = vertex("INE5422",4)

		INE5427 = vertex("INE5427",4)
		INE5453 = vertex("INE5453",4)
		INE5425 = vertex("INE5425",4)
		INE5430 = vertex("INE5430",4)
		INE5426 = vertex("INE5426",4)
		INE5424 = vertex("INE5424",4)

		INE5433 = vertex("INE5433",6)
		INE5432 = vertex("INE5432",4)
		INE5429 = vertex("INE5429",4)
		INE5431 = vertex("INE5431",4)
		INE5428 = vertex("INE5428",4)

		INE5434 = vertex("INE5434",6)

		gnew.add_vertex(INE5402)
		gnew.add_vertex(MTM5161)
		gnew.add_vertex(INE5403)
		gnew.add_vertex(EEL5105)
		gnew.add_vertex(INE5401)
		gnew.add_vertex(INE5404)
		gnew.add_vertex(MTM7174)
		gnew.add_vertex(INE5405)
		gnew.add_vertex(MTM5512)
		gnew.add_vertex(INE5406)
		gnew.add_vertex(INE5407)
		gnew.add_vertex(INE5408)
		gnew.add_vertex(INE5410)
		gnew.add_vertex(INE5409)
		gnew.add_vertex(MTM5245)
		gnew.add_vertex(INE5411)
		gnew.add_vertex(INE5417)
		gnew.add_vertex(INE5413)
		gnew.add_vertex(INE5415)
		gnew.add_vertex(INE5416)
		gnew.add_vertex(INE5412)
		gnew.add_vertex(INE5414)
		gnew.add_vertex(INE5419)
		gnew.add_vertex(INE5423)
		gnew.add_vertex(INE5420)
		gnew.add_vertex(INE5421)
		gnew.add_vertex(INE5418)
		gnew.add_vertex(INE5422)
		gnew.add_vertex(INE5427)
		gnew.add_vertex(INE5453)
		gnew.add_vertex(INE5425)
		gnew.add_vertex(INE5430)
		gnew.add_vertex(INE5426)
		gnew.add_vertex(INE5424)
		gnew.add_vertex(INE5433)
		gnew.add_vertex(INE5432)
		gnew.add_vertex(INE5429)
		gnew.add_vertex(INE5431)
		gnew.add_vertex(INE5428)
		gnew.add_vertex(INE5434)

if __name__ == "__main__":
	main()
