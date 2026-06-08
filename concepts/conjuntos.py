graphicDesigner = set([
    'InDesign',
    'Photoshop',
    'Acrobat',
    'Premiere',
    'Bridge',
])
graphicDesigner.add('Illustrator')
# Caso não exita no set dá KeyError
graphicDesigner.remove('Bridge')
# Caso não exista ele não dá erro
graphicDesigner.discard('Muse')
print(graphicDesigner)
# Remover e retornar
graphicDesigner.pop()

graphicDesigner.clear()

print(graphicDesigner)

# Initialize 3 sets
set1 = set([7, 10, 11, 13])
set2 = set([11, 8, 9, 12, 14, 15])
set3 = {'d', 'f', 'h'}

# Update set1 with set2
set1.update(set2)
print(set1)

# Update set1 with set3
set1.update(set3)
print(set1)

# Remove duplicado automaticamente
print(list(set([1, 2, 3, 1, 7])))

"""
Operações de Conjuntos
"""
# União
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

# set built-in function union
dataScientist.union(dataEngineer)

# Se trata de uma união, igual ao de cima
print(dataScientist | dataEngineer)

# Intersection operation
dataScientist.intersection(dataEngineer)

# Equivalent Result
print(dataScientist & dataEngineer)
