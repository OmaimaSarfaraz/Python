# Union (| or union())
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)              # {1, 2, 3, 4, 5}
print(a.union(b))         # {1, 2, 3, 4, 5}


# Intersection (& or intersection())
print(a & b)              # {3}
print(a.intersection(b))  # {3}


# Difference (- or difference())
print(a - b)              # {1, 2}
print(b - a)              # {4, 5}


# Symmetric Difference (^ or symmetric_difference())
print(a ^ b)                     # {1, 2, 4, 5}
print(a.symmetric_difference(b)) # {1, 2, 4, 5}


# Subset & Superset
x = {1, 2}
y = {1, 2, 3, 4}
print(x.issubset(y))   # True
print(y.issuperset(x)) # True


# Disjoint Sets
p = {1, 2}
q = {3, 4}
print(p.isdisjoint(q))   # True