medida_tornillo = float(input())

if medida_tornillo >= 1.0 and medida_tornillo <= 2.9:
    print('El tornillo es pequeno.')
elif medida_tornillo >= 3.0 and medida_tornillo < 5.0:
    print('El tornillo es mediano.')
elif medida_tornillo >= 5.0 and medida_tornillo < 6.5:
    print('El tornillo es grande.')
elif medida_tornillo >= 6.5 and medida_tornillo <= 8.5:
    print('El tornillo es muy grande.')
elif medida_tornillo > 8.5:
    print('El tornillo es gigante.')
else:
    print('El tamano ingresado no es valido.')