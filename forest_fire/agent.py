from mesa import Agent


class TreeCell(Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Fine"
        self.ext_prob = model.ext_prob
        self.rnw_fact = model.rnw_fact

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """
        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                self.random.random()
                if neighbor.condition == "Fine" and self.random.random() > self.ext_prob: #Probabilidade de extinção do fogo antes de passar para a próxima árvore.
                    neighbor.condition = "On Fire"
                self.condition = "Burned Out"

            
                
            for posi in self.model.grid.iter_neighborhood(self.pos, moore=True, include_center=True):
                if (self.model.grid.is_cell_empty(posi) and self.random.random() < self.rnw_fact):
                        new_tree = TreeCell((posi), self)
                        new_tree.condition = "Renewed"

                        self.model.grid._place_agent((posi), new_tree)
                        self.model.schedule.add(new_tree)

            self.condition = "Burned Out"
            
