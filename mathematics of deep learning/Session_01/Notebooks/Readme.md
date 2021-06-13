# Workshop Quiz 1


    - Do feed-forward neural networks accept only fixed size inputs or can they accommodate variable size inputs? Explain your answer

    - You are trying to implement a 2-input Boolean AND gate using neural networks. Do you need a non-linear activation function for this or will a linear model do? Motivate your answer

    - If Input = Tensor([[x1, x2, x3], [x4, x5, x6], [x7, x8, x9]]) , how do you use PyTorch to return a view of this tensor such that the resulting tensor has shape 2 X 2 with elements x1 and x3 in one row and x2 and x4 in another?

    - Write an efficient way of creating a PyTorch tensor containing all the powers of 2 that are less that are less than the number 100

    - x.shape = torch.Size([20, 50]) and x_lengths.shape = torch.size([20]). x_lengths contains the lengths of each of the 20 samples. Each element in the sample (There are 50 elements per sample) is divided by the corresponding length. How can you achieve this in PyTorch?

    - When 2 vectors are perpendicular to each other, the dot product is
        - 1
        - 0
        - -1
        - Data insufficient

    - Matrix multiplication of a 3 * 2 matrix with a 4 * 4 matrix is possible or not? If not possible, what should the size of the second matrix be to make the multiplication possible?
        - 3 * N
        - 3 * 2
        - 2 * N
        - N * 3

    - If the determinant of a matrix is zero,
        - The matrix is invertible
        - The matrix is not invertible
        - Insufficient info

    - From an optimizaton standpoint, which is more desirable?
        - All eigen values are positive
        - All eigen values are negative
        - Doesn't matter either way
        - Mixture of positive and negative eigen values, centered around zero

    - Which of these activation is generally the least computationally intensive?
        - Sigmoid 
        - ReLu
        - Softmax
        - Tanh