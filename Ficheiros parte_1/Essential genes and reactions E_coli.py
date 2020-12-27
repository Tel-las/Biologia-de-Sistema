from cobra.io import read_sbml_model
model = read_sbml_model('iML1515.xml')
from mewpy.simulation import get_simulator
simul = get_simulator(model)
for i in simul.essential_reactions:
    print(i)
print('------------------------------------------')
for i in simul.essential_genes:
    print(i)