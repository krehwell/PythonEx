def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
        return "%s is benefit of the function" % benefit

def printBenefitz():
    for benefit in list_benefits():
        print(build_sentence(benefit))

printBenefitz()