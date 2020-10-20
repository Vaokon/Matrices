using System;

namespace Linear_algebra
{
    class Program
    {
        static void Main(string[] args)
        {
            Matrix A = new Matrix(new double[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } });
            Matrix B = new Matrix(new double[,] { { 1, 0, 0 }, { 0, 0, 1 }, { 0, 1, 0 } });
            Matrix C = new Matrix(new double[,] { { 1, 0, 5 }, { 4, 0, 42 }, { 8, 0, 1 } });
            Matrix D = new Matrix(new double[,] { { 1, 1 }, { 4, 0 } });
            Matrix E = new Matrix(new double[,] { { 1, 0 } });
            Matrix F = new Matrix(new double[,] { { 25 } });
            Matrix G = new Matrix(new double[,] { { 6, 1, 1 }, { 4, -2, 5 }, { 2, 8, 7 } });
            Matrix H = new Matrix(new double[,] { { 1, 2, 1, 0 }, { 0, 3, 1, 1 }, { -1, 0, 3, 1 }, { 3, 1, 2, 0 } });
            Matrix I = new Matrix(new double[,] { { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } });
            Matrix M = new Matrix(new double[,] { { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 1 } });
            A.Print();
            Matrix Added_matrix = A.Add(B);
            Added_matrix.Print();

        }
    }
    class Matrix
    {
        public double[,] matrix_array;
        private int nb_rows_array;
        private int nb_columns_array;
        public Matrix(double[,] matrix_input)
        {
            matrix_array = matrix_input;
            nb_rows_array = matrix_array.GetLength(0);
            nb_columns_array = matrix_array.GetLength(1);
        }

        public void Print()
        {
            for (int i = 0; i < nb_rows_array; i++)
            {
                for (int j = 0; j < nb_columns_array; j++)
                {
                    Console.Write(matrix_array[i, j] + " ");
                }

                Console.WriteLine();
            }
        }
        public Matrix Add(Matrix other_matrix)
        {   //checks if both matrices are of the same size
            //if (nb_rows_array != other_matrix.nb_rows_array ^ nb_columns_array != other_matrix.nb_columns_array);  
            double[,] temp_matrix_array = new double[nb_rows_array, nb_columns_array];
            for (int i = 0; i < nb_rows_array; i++)
            {
                for (int j = 0; j < nb_columns_array; j++)
                {
                    temp_matrix_array[i, j] = matrix_array[i, j] + other_matrix.matrix_array[i, j];
                }
            }
            return new Matrix(temp_matrix_array);
        }
        public Matrix Substract(Matrix other_matrix)
        {
            return Add(other_matrix.Multiply(-1));
        }

        public Matrix Multiply(double constant)
        {
            double[,] temp_matrix_array = new double[nb_rows_array, nb_columns_array];
            for (int i = 0; i < nb_rows_array; i++)
            {
                for (int j = 0; j < nb_columns_array; j++)
                {
                    temp_matrix_array[i, j] = constant * matrix_array[i, j];
                }
            }
            return new Matrix(temp_matrix_array);
        }

        public Matrix Multiply(Matrix other_matrix)
        {
            double[,] output_array = new double[nb_rows_array, other_matrix.nb_columns_array];
            for (int output_row = 0; output_row < nb_rows_array; output_row++)
            {
                for (int output_column = 0; output_column < nb_columns_array; output_column++)
                {
                    double sum = 0;
                    for (int i = 0; i < other_matrix.nb_rows_array; i++)
                    {
                        sum += matrix_array[output_row, i] * other_matrix.matrix_array[i, output_column];
                    }
                    output_array[output_row, output_column] = sum;
                }
            }
            return new Matrix(output_array);

        }

        public Matrix Divide(double constant)
        {
            return Multiply(1 / constant);
        }

        public Matrix Power(int exponent)
        {
            Matrix temp_matrix = new Matrix((double[,])matrix_array.Clone());
            for (int i = 0; i < exponent - 1; i++)
            {
                temp_matrix = temp_matrix.Multiply(new Matrix(matrix_array));
            }
            return temp_matrix;
        }

        public Matrix Transpose()
        {
            double[,] output_array = new double[nb_columns_array, nb_rows_array];
            for (int i = 0; i < nb_rows_array; i++)
            {
                for (int j = 0; j < nb_columns_array; j++)
                {
                    output_array[j, i] = matrix_array[i, j];
                }
            }
            return new Matrix(output_array);
        }

        public Matrix LeftOverMatrix(int row, int column)
        {
            
            double[,] temp_matrix_array = new double[nb_rows_array-1, nb_columns_array-1];
             for (int i=0; i<temp_matrix_array.GetLength(0); i ++)
            {
                for (int j = 0; j<temp_matrix_array.GetLength(1); j ++)
                {
                    if (i < row & j < column)
                    {
                        temp_matrix_array[i, j] = matrix_array[i, j];
                    }
                    if (i>row & j>row)
                    {
                        temp_matrix_array[i-1, j-1] = matrix_array[i, j];
                    }
                }
            }
            return new Matrix(temp_matrix_array);
        }

        public double Determinant()
        {
            if (nb_rows_array == 1)
            {
                return (float)matrix_array[0,0];
            }
            if (nb_rows_array ==2 )
            {
                return (float)matrix_array[0,0] * matrix_array[1,1] - matrix_array[1,0] * matrix_array [0,1];
            }
            else
            {
                double det = 0;
                for (int j = 0; j<nb_rows_array; j++)
                {
                    int sign;
                    if (j%2 == 1)
                    {
                        sign = -1;
                    }
                    else
                    {
                        sign = 1;
                    }
                    Matrix small_matrix = LeftOverMatrix(0, j);
                    det += sign * matrix_array[0, j] * small_matrix.Determinant();

                }
                return det;
            }
        }

        public double Minor(int row, int column)
        {
            return new Matrix(LeftOverMatrix(row, column).matrix_array).Determinant();
        }

        public Matrix MinorsMatrix()
        {
            double[,] output_matrix_array = new double[nb_rows_array, nb_columns_array];
            for (int i = 0; i<nb_rows_array;i++)
            {
                for (int j = 0; j<nb_columns_array;j++)
                {
                    output_matrix_array[i,j] = Minor(i, j);
                }
            }
            return new Matrix(output_matrix_array);
        }
        
        public double Cofactor(int row, int column)
        {
            return Math.Pow(-1, row+column) * Minor(row, column);
        }

        public Matrix CofactorMatrix()
        {
            double[,] output_matrix_array = new double[nb_rows_array, nb_columns_array];
            for (int i = 0; i<nb_rows_array;i++)
            {
                for (int j = 0; j<nb_columns_array; j++)
                {
                    output_matrix_array[i,j] = Cofactor(i,j);
                }
            }
            return new Matrix(output_matrix_array);
        }

        public double Trace()
        {
            double output = 0;
            for (int i = 0; i<nb_rows_array; i++)
            {
                output += matrix_array[i, i];
            }
            return output;
        }

        public Matrix AdjointMatrix()
        {
            return CofactorMatrix().Transpose();
        }

        public Matrix Inverse_Matrix()
        {
            double det = Determinant();
            return AdjointMatrix().Divide(det);
        }
    }
}