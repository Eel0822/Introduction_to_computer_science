def parse_matrix(matrix_str):
    #對於輸入的文字去分析
    matrix = {}
    rows = matrix_str.strip().split('|')
    n = len(rows)
    for i, row in enumerate(rows):
        elements = row.strip().split(',')
        for j, element in enumerate(elements):
            matrix[(i, j)] = int(element)
    return matrix, n

def multiply_matrices(U, V, n):
    #計算兩個矩陣的外積值，並放入字典中
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U.get((i, k), 0) * V.get((k, j), 0) for k in range(n))
    return M

def matrix_to_list(M, n):
    #將字典轉換為矩陣形式呈現
    matrix_list = []
    for i in range(n):
        row = [M.get((i, j), 0) for j in range(n)]
        matrix_list.append(row)
    return matrix_list

def main():
    #輸入第一個和第二個矩陣
    U_str = input("Enter matrix U: ")
    V_str = input("Enter matrix V: ")

    #透過function分析矩陣
    U, n = parse_matrix(U_str)
    V, _ = parse_matrix(V_str)

    #計算矩陣外積
    M = multiply_matrices(U, V, n)

    #依照格式輸出矩陣
    print("M = U x V")
    result = matrix_to_list(M, n)
    for row in result:
        print(row)

if __name__ == "__main__":
    main()