import numpy as np

def Array():
    arr = np.array([[1, 2], [3, 4]])

    eigenvalues, eigenvectors = np.linalg.eig(arr)
    determinant = np.linalg.det(arr)

    print("eigenvalues:")
    print(eigenvalues)
    print("eigenvectors:")
    print(eigenvectors)
    print("determinant:")
    print(determinant)

    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])

    cross_product = np.cross(vec1, vec2)

    print("cross product:")
    print(cross_product)


    A = np.array([[1, 2, -2], [2, 1, 5], [1, -4, 1]])
    b = np.array([-15, -21, 18])

    solutions = np.linalg.solve(A, b)

    print("solutions:")
    print(solutions)

if __name__ == "__main__":
    Array()
