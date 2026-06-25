class CoalAgent:
    def __init__(self):
        self.knowledge = {
            "reserves": "Telangana has approximately 23.29 billion tonnes of coal reserves, mainly in the Godavari Valley coalfields.",
            "sccl": "Singareni Collieries Company Limited (SCCL) is the major coal mining company in Telangana.",
            "districts": "Major coal-bearing districts include Bhadradri Kothagudem, Mancherial, Peddapalli, and Jayashankar Bhupalpally.",
            "technology": "Modern mining technologies include draglines, longwall mining, and conveyor-based coal transport."
        }

    def process(self, query):
        query = query.lower()

        if "reserve" in query or "coal" in query:
            return self.knowledge["reserves"]

        elif "sccl" in query or "company" in query:
            return self.knowledge["sccl"]

        elif "district" in query or "where" in query:
            return self.knowledge["districts"]

        elif "technology" in query or "equipment" in query:
            return self.knowledge["technology"]

        return "Coal Agent could not find a relevant answer."