{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-DoXWN8VamJa"
      },
      "source": [
        "# Python Bootcamp: Assignment 3 [100 points]\n",
        "\n",
        "This week we will start writing some code! This assignment is designed to be a crash-course to get you up to speed on the level of Python you will need to know in order to do the remainder of the assignments. It's easiest to learn by doing, so please start early so we can help you get on board. You want to spend the semester focusing on the crowdsourcing and machine learning, not the indenting and semicoloning.\n",
        "\n",
        "Before you do anything save a copy of this file in Drive (found in File) and work on that one."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5p5mAqq8ZNh3"
      },
      "source": [
        "## 1. Working with Lists [15 points]\n",
        "\n",
        "1. **[5 points]** Consider the function `extract_and_apply(l, p, f)` shown below, which extracts the elements of a list `l` satisfying a boolean predicate `p`, applies a function f to each such element, and returns the result.\n",
        "\n",
        "  Rewrite `extract_and_apply(l, p, f)` in one line using a list comprehension."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VaIiupCGOs05"
      },
      "source": [
        "def extract_and_apply(l, p, f):\n",
        "     result = []\n",
        "     for x in l:\n",
        "         if p(x):\n",
        "             result.append(f(x))\n",
        "     return result"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O2SPSqSNJzkw"
      },
      "source": [
        "def extract_and_apply(l, p, f):\n",
        "    return [f(x) for x in l if p(x)]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SfgvlZJ2avES",
        "outputId": "ff9a21f8-4af2-4125-82b5-06aec41d3d9c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# # Example:\n",
        "l = [1, 2, 3, 4]\n",
        "p = lambda x: x % 2 == 0\n",
        "f = lambda x: x\n",
        "extract_and_apply(l, p, f)\n",
        "\n",
        "# # Expected output:\n",
        "# # [2, 4]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[2, 4]"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Nec_sUYwOWBk"
      },
      "source": [
        "2. **[5 points]** Write a function `concatenate(seqs)` that returns a list containing the concatenation of the elements of the input sequences. Your implementation should consist of a single list comprehension, and should not exceed one line.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4p-SsgwCaNNL"
      },
      "source": [
        "def concatenate(seqs):\n",
        "    return [item for seq in seqs for item in seq]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Eh_BZSUIOmQM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6f8bf8a9-d928-4a6b-da51-a932b98edb7b"
      },
      "source": [
        "# # Example:\n",
        "concatenate([[1, 2], [3, 4]])\n",
        "\n",
        "# # Expected output:\n",
        "# # [1, 2, 3, 4]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4]"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1idmVGakO6Y7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "02c81c9e-90ce-4684-8304-8bca16d0e0cf"
      },
      "source": [
        "# # Example:\n",
        "concatenate([\"abc\", (0, [0])])\n",
        "\n",
        "# # Expected output:\n",
        "# # ['a', 'b', 'c', 0, [0]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['a', 'b', 'c', 0, [0]]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bxE4OG0sO_mL"
      },
      "source": [
        "3. **[5 points]** Write a function `transpose(matrix)` that returns the transpose of the input matrix, which is represented as a list of lists. Recall that the transpose of a matrix is obtained by swapping its rows with its columns. More concretely, the equality `matrix[i][j] == transpose(matrix)[j][i`] should hold for all valid indices `i` and `j`. You may assume that the input matrix is well-formed, i.e., that each row is of equal length. You may further assume that the input matrix is non-empty. Your function should not modify the input."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xXgNgjIgO9zu"
      },
      "source": [
        "def transpose(matrix):\n",
        "    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6RuBAwyNQgAq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d312503e-5b5e-43a1-d52c-b11449fae667"
      },
      "source": [
        "# # Example:\n",
        "transpose([[1, 2, 3]])\n",
        "\n",
        "# # Expected output:\n",
        "# # [[1], [2], [3]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[1], [2], [3]]"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "abVIxUH4Qm_y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6ff0a94c-b9c9-47e9-fec0-b3b32619a11d"
      },
      "source": [
        "# # Example:\n",
        "transpose([[1, 2], [3, 4], [5, 6]])\n",
        "\n",
        "# # Expected output:\n",
        "# # [[1, 3, 5], [2, 4, 6]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[1, 3, 5], [2, 4, 6]]"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BPVQUfMZPVH8"
      },
      "source": [
        "## 2. Sequence Slicing [9 points]\n",
        "\n",
        "The functions in this section should be implemented using sequence slices. Recall that the slice parameters take on sensible default values when omitted. In some cases, it may be necessary to use the optional third parameter to specify a step size."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8F8xbe22PrjN"
      },
      "source": [
        "1. **[3 points]** Write a function `copy(seq)` that returns a new sequence containing the same elements as the input sequence."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_c8quuKaP1kr"
      },
      "source": [
        "def copy(seq):\n",
        "    return seq[:]"
      ],
      "execution_count": 52,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fDwiXbgSQ2kl",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "c25474ba-6699-469f-82eb-8b607eef694e"
      },
      "source": [
        "# # Example:\n",
        "copy(\"abc\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'abc'"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'abc'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AgJniWKiTo50",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "66431918-31ac-4d65-b7ee-bdc1823bcb20"
      },
      "source": [
        "# # Example:\n",
        "copy((1, 2, 3))\n",
        "\n",
        "# # Expected output:\n",
        "# #  (1, 2, 3)"
      ],
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1, 2, 3)"
            ]
          },
          "metadata": {},
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B3x-6vYgTt9_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "81ffaae3-1917-44dc-e552-bc541063a2e4"
      },
      "source": [
        "# # Example:\n",
        "x = [0, 0, 0]\n",
        "y = copy(x)\n",
        "print(x, y)\n",
        "\n",
        "x[0] = 1\n",
        "print(x, y)\n",
        "\n",
        "# # Expected output:\n",
        "# # [0, 0, 0] [0, 0, 0]\n",
        "# # [1, 0, 0] [0, 0, 0]"
      ],
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 0, 0] [0, 0, 0]\n",
            "[1, 0, 0] [0, 0, 0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EWFsSPU9P8qk"
      },
      "source": [
        "2. **[3 points]** Write a function `all_but_last(seq)` that returns a new sequence containing all but the last element of the input sequence. If the input sequence is empty, a new empty sequence of the same type should be returned."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9jwUCABhQrDc"
      },
      "source": [
        "def all_but_last(seq):\n",
        "    return seq[:-1]\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QX5KvmFoUBE_",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "27074e15-11b5-409d-a375-e9608070b8bf"
      },
      "source": [
        "# # Example:\n",
        "all_but_last(\"abc\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'ab'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'ab'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FP1-RCwNUBnG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f3332eec-da6b-4dfe-d5d5-817c97757ac4"
      },
      "source": [
        "# # Example:\n",
        "all_but_last((1, 2, 3))\n",
        "\n",
        "# # Expected output:\n",
        "# # (1, 2)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1, 2)"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6grrejDpUFVc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "2ee962c6-aafc-495b-f2de-df451e71949c"
      },
      "source": [
        "# # Example:\n",
        "all_but_last(\"\")\n",
        "\n",
        "# # Expected output:\n",
        "# # ''"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "''"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PPy1_MmaUFxc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28104616-0c5a-4b6a-ada1-da13cd138cdb"
      },
      "source": [
        "# # Example:\n",
        "all_but_last([])\n",
        "\n",
        "# # Expected output:\n",
        "# # []"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[]"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mlazyiLVQA90"
      },
      "source": [
        "3. **[3 points]** Write a function `every_other(seq)` that returns a new sequence containing every other element of the input sequence, starting with the first. This function can be written in one line using the optional third parameter of the slice notation."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HjMNQZg2P_9A"
      },
      "source": [
        "def every_other(seq):\n",
        "    return seq[::2]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IHruD_R_QGfh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0cb5b73a-92fb-42b1-e100-2d2b59136892"
      },
      "source": [
        "# # Example:\n",
        "every_other([1, 2, 3, 4, 5])\n",
        "\n",
        "# # Expected output:\n",
        "# # [1, 3, 5]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 3, 5]"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9tqzrxB-USB9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "6ecd76b6-64b6-4e6b-8fd4-0f6c7cafc18e"
      },
      "source": [
        "# # Example:\n",
        "every_other(\"abcde\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'ace'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'ace'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-uQO2ygIUWqV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4cdf759d-3b5a-4410-f27f-af413835bd76"
      },
      "source": [
        "# # Example:\n",
        "every_other([1, 2, 3, 4, 5, 6])\n",
        "\n",
        "# # Expected output:\n",
        "# # [1, 3, 5]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 3, 5]"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "st2VKKSwUXJx",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "d657967c-3389-4a1a-b2fe-44d738dcb85c"
      },
      "source": [
        "# # Example:\n",
        "every_other(\"abcdef\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'ace'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'ace'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eDAwdnKrQ7vw"
      },
      "source": [
        "## 3. Combinatorial Algorithms [12 points]\n",
        "\n",
        "The functions in this section should be implemented as generators. You may generate the output in any order you find convenient, as long as the correct elements are produced. However, in some cases, you may find that the order of the example output hints at a possible implementation.\n",
        "\n",
        "Although generators in Python can be used in a variety of ways, you will not need to use any of their more sophisticated features here. Simply keep in mind that where you might normally return a list of elements, you should instead yield the individual elements.\n",
        "\n",
        "Since the contents of a generator cannot be viewed without employing some form of iteration, we wrap all function calls in this section’s examples with the list function for convenience."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yYtgo8_pRIGD"
      },
      "source": [
        "1. **[6 points]** The prefixes of a sequence include the empty sequence, the first element, the first two elements, etc., up to and including the full sequence itself. Similarly, the suffixes of a sequence include the empty sequence, the last element, the last two elements, etc., up to and including the full sequence itself. Write a pair of functions `prefixes(seq)` and `suffixes(seq)` that yield all prefixes and suffixes of the input sequence."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UMGYij6TRS3t"
      },
      "source": [
        "def prefixes(seq):\n",
        "    for i in range(len(seq) + 1):\n",
        "        yield seq[:i]\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JM_wRlleRdt3"
      },
      "source": [
        "def suffixes(seq):\n",
        "    for i in range(len(seq) + 1):\n",
        "        yield seq[i:]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I-LDSa0eUwn5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "24bf8fa8-569b-4f4e-cd97-6000d8c4d393"
      },
      "source": [
        "# # Example:\n",
        "list(prefixes([1, 2, 3]))\n",
        "\n",
        "# # Expected output:\n",
        "# # [[], [1], [1, 2], [1, 2, 3]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[], [1], [1, 2], [1, 2, 3]]"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GoMR516HUxm7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1053ad4b-63c2-414e-94c0-5986c71e1a59"
      },
      "source": [
        "# # Example:\n",
        "list(suffixes([1, 2, 3]))\n",
        "\n",
        "# # Expected output:\n",
        "# # [[1, 2, 3], [2, 3], [3], []]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[1, 2, 3], [2, 3], [3], []]"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wXn7fZB7Uzq7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1663294d-98af-4040-a832-21797130a822"
      },
      "source": [
        "# # Example:\n",
        "list(prefixes(\"abc\"))\n",
        "\n",
        "# # Expected output:\n",
        "# # ['', 'a', 'ab', 'abc']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['', 'a', 'ab', 'abc']"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LvzQVX5iU071",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cc0efeb1-4454-4edf-fadc-3133d52b58c9"
      },
      "source": [
        "# # Example:\n",
        "list(suffixes(\"abc\"))\n",
        "\n",
        "# # Expected output:\n",
        "# # ['abc', 'bc', 'c', '']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['abc', 'bc', 'c', '']"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UnIWnd7bRVpC"
      },
      "source": [
        "2. **[6 points]** Write a function `slices(seq)` that yields all non-empty slices of the input sequence."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k2lmNjY9RaFy"
      },
      "source": [
        "def slices(seq):\n",
        "    for i in range(len(seq)):\n",
        "        for j in range(i + 1, len(seq) + 1):\n",
        "            yield seq[i:j]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BQRgX51NVEE4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f822f79d-5840-47df-8fef-68a3bac61056"
      },
      "source": [
        "# # Example:\n",
        "list(slices([1, 2, 3]))\n",
        "\n",
        "# # Expected output:\n",
        "# # [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C5qnTbTgVFta",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "14f2ef63-234a-46c0-f71b-630a0747d7e3"
      },
      "source": [
        "# # Example:\n",
        "list(slices(\"abc\"))\n",
        "\n",
        "# # Expected output:\n",
        "# # ['a', 'ab', 'abc', 'b', 'bc', 'c']"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['a', 'ab', 'abc', 'b', 'bc', 'c']"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XeIbx4rqRmUO"
      },
      "source": [
        "## 4. Text Processing [20 points]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "S2gAcwQZRrcv"
      },
      "source": [
        "1. **[5 points]** A common preprocessing step in many natural language processing tasks is text normalization, wherein words are converted to lowercase, extraneous whitespace is removed, etc. Write a function `normalize(text)` that returns a normalized version of the input string, in which all words have been converted to lowercase and are separated by a single space. No leading or trailing whitespace should be present in the output."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ex7WetNTRvLm"
      },
      "source": [
        "def normalize(text):\n",
        "    return ' '.join(text.lower().split())"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d-kXSmbsVx0i",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "2d8ffb6d-e866-43ae-a111-b8e9c95aa397"
      },
      "source": [
        "# # Example:\n",
        "normalize(\"This is an example.\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'this is an example.'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'this is an example.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qfHFoK8hVzOp",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "c89ce68f-3c0d-4bff-c394-1b2662a296ce"
      },
      "source": [
        "# # Example:\n",
        "normalize(\"   EXTRA   SPACE   \")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'extra space'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'extra space'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 38
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nERQLA3_RxPy"
      },
      "source": [
        "2. **[5 points]** Write a function `no_vowels(text)` that removes all vowels from the input string and returns the result. For the purposes of this problem, the letter ‘y’ is not considered to be a vowel.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IMg2KKn5R5Jf"
      },
      "source": [
        "def no_vowels(text):\n",
        "    vowels = \"aeiouAEIOU\"\n",
        "    return ''.join(char for char in text if char not in vowels)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "b58SNc5fV5PY",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "edf6a911-40c9-409b-d491-9f7f302d8e94"
      },
      "source": [
        "# # Example:\n",
        "no_vowels(\"This Is An Example.\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'Ths s n xmpl.'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Ths s n xmpl.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cum2PhkwV6zI",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "db9d48b1-04df-4f96-c4c1-3fb242a0d6e4"
      },
      "source": [
        "# # Example:\n",
        "no_vowels(\"We love Python!\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'W lv Pythn!'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'W lv Pythn!'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NXuzhUvbR1pm"
      },
      "source": [
        "3. **[5 points]** Write a function `digits_to_words(text)` that extracts all digits from the input string, spells them out as lowercase English words, and returns a new string in which they are each separated by a single space. If the input string contains no digits, then an empty string should be returned."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "x_s2GQraR-g7"
      },
      "source": [
        "def digits_to_words(text):\n",
        "    digit_words = {\n",
        "        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',\n",
        "        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'\n",
        "    }\n",
        "    digits = [char for char in text if char.isdigit()]\n",
        "    return ' '.join(digit_words[digit] for digit in digits)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QGnzPb7dV-Gr",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "04726b0a-782d-49be-f7e5-6da8d8a1528a"
      },
      "source": [
        "# # Example:\n",
        "digits_to_words(\"Zip Code: 19104\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'one nine one zero four'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'one nine one zero four'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y-Ig9XxVWAa5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "b2e29997-54f5-48af-f6cf-7b3c5141ade3"
      },
      "source": [
        "# # Example:\n",
        "digits_to_words(\"Pi is 3.1415...\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'three one four one five'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'three one four one five'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# # Example:\n",
        "digits_to_words(\"Pi is number\")\n",
        "# # Expected output:\n",
        "# # ''"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "wjShSVG4c6iH",
        "outputId": "6f3ebd93-8beb-48fa-fed9-ad6eac7b6607"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "''"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TVjzVXPKSFNE"
      },
      "source": [
        "4. **[5 points]** Although there exist many naming conventions in computer programming, two of them are particularly widespread. In the first, words in a variable name are separated using underscores. In the second, words in a variable name are written in mixed case, and are strung together without a delimiter. By mixed case, we mean that the first word is written in lowercase, and that subsequent words have a capital first letter. Write a function `to_mixed_case(name)` that converts a variable `name` from the former convention to the latter. Leading and trailing underscores should be ignored. If the variable name consists solely of underscores, then an empty string should be returned.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vx4LCUUNSJzL"
      },
      "source": [
        "def to_mixed_case(name):\n",
        "    parts = name.strip('_').split('_')\n",
        "    parts = [part for part in parts if part]\n",
        "\n",
        "    if not parts:\n",
        "        return ''\n",
        "\n",
        "    result = parts[0].lower()\n",
        "    for part in parts[1:]:\n",
        "        result += part.capitalize()\n",
        "\n",
        "    return result"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vs3oWE6pWKyj",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "032f7915-ef7e-4728-f3a6-e16501d41d79"
      },
      "source": [
        "# # Example:\n",
        "to_mixed_case(\"to_mixed_case\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'toMixedCase'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'toMixedCase'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vLYKR57PWMXn",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "31b600a9-a870-4632-8981-992eee5b02b4"
      },
      "source": [
        "# # Example:\n",
        "to_mixed_case(\"__EXAMPLE__NAME__\")\n",
        "\n",
        "# # Expected output:\n",
        "# # 'exampleName'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'exampleName'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RLjrVt6ci-0n"
      },
      "source": [
        "## 5. DataFrames [44 points]\n",
        "In this section you'll get a feel for pandas' DataFrames a datastructure similar to SQL tables that can directly read lists and csvs and supports a number of optimized operations."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RQuSqzQpg4Rk"
      },
      "source": [
        "### 5.1 Manipulating a csv [30 points]\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "11tqRwRjjPDP"
      },
      "source": [
        "# first we'll import pandas\n",
        "import pandas as pd"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7BBzP7VT7TVw"
      },
      "source": [
        "1. **[2 points]** In the method `read_file` create a dataframe from the given csv file."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4jSbGErU7ZED"
      },
      "source": [
        "# hint: look at the pandas method read_csv\n",
        "def read_file(file):\n",
        "    \"\"\"\n",
        "    Returns\n",
        "    -------\n",
        "    Dataframe created from the given file\n",
        "    \"\"\"\n",
        "    return pd.read_csv(file)"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s6XXVSGjjRxM"
      },
      "source": [
        "df = read_file('batch.csv')"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oULq5P61kOM-"
      },
      "source": [
        "batch.csv is a csv of the results from a batch of HITs on MTurk. With it you can see worker Ids, their answers to each question, as well as their accept and submit times.\n",
        "\n",
        "Comment the cells below out before you submit."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NcUBr8I2kAu3"
      },
      "source": [
        "# you can also get a smaller glimpse with\n",
        "#display (df.head())"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CLkmAGwUkGCu"
      },
      "source": [
        "# or just the columns with\n",
        "#display (df.columns)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HdHdDvEU-YP_"
      },
      "source": [
        "# a slice of a dataframe is called a series. for example:\n",
        "#display (df['HITId'])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W_CfaUJ18SY-"
      },
      "source": [
        "2. **[3 points]** Write the method `get_workerId_by_row` that returns the Worker ID at the given row in the dataframe."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rWmwR6KC4eXv"
      },
      "source": [
        "def get_workerId_by_row(df, row):\n",
        "    return df.loc[row, 'WorkerId']"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jLm321SL4zF0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "1df098cb-17f2-4623-82fe-8ee400ffb665"
      },
      "source": [
        "# EXAMPLE\n",
        "get_workerId_by_row(df, 3)\n",
        "# 'A98E8M4QLI9RS'"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'A98E8M4QLI9RS'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b5vS53dA85b0"
      },
      "source": [
        "3. **[5 points]** In the method `format_date` convert a datetime string from the format Year-Month-Day Hour-Minute-Second to a timestamp in minutes."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lhJUDzAm5J83"
      },
      "source": [
        "# TODO\n",
        "# convert the given date into a timestamp (in seconds)\n",
        "from datetime import datetime\n",
        "def format_date(date):\n",
        "    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')\n",
        "    timestamp_seconds = dt.timestamp()\n",
        "    minutes = timestamp_seconds / 60\n",
        "    return minutes"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "72GOuXPjV_HE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "23baf6d1-1fe9-474e-f4dc-98308e645447"
      },
      "source": [
        "# EXAMPLE\n",
        "format_date('2020-02-06 23:25:41')\n",
        "#-> 26350525.683333334"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "26350525.683333334"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i8XZnksr-FlD"
      },
      "source": [
        "4. **[5 points]** Use the `format_date` method to convert each entry in `SubmitTime` and `AcceptTime` into a timestamp. In `convert_times` return the series you get by applying that method to each entry in the given column"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "locQGkg7-fsi"
      },
      "source": [
        "# hint: look at the dataframe apply method\n",
        "def convert_times(df, column):\n",
        "    return df[column].apply(format_date)"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V5K2Skwv_wJa"
      },
      "source": [
        "# comment these out before you submit\n",
        "#df['SubmitTime'] = convert_times(df, 'SubmitTime')\n",
        "#df['AcceptTime'] = convert_times(df, 'AcceptTime')"
      ],
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HT_NiDhq99vv"
      },
      "source": [
        "5. **[5 points]** In `get_work_time` figure out how long each worker spent on the batch. Return the series that is the total work time indexed by the worker id."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A_TO5PiT50Mr"
      },
      "source": [
        "# hint: look at the dataframe groupby function\n",
        "def get_work_time(df):\n",
        "    df['WorkDuration'] = df['SubmitTime'] - df['AcceptTime']\n",
        "    work_times = df.groupby('WorkerId')['WorkDuration'].sum()\n",
        "    return work_times"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eup_0ZYfWe3O",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "outputId": "fa030e7b-b2eb-4abf-e7a0-71e345049a87"
      },
      "source": [
        "# EXAMPLE\n",
        "get_work_time(df)\n",
        "# Should be a series like\n",
        "# Time\n",
        "# Time"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "WorkerId\n",
              "A1CY7IOJ9YH136     14.016667\n",
              "A2C84POENS2UNY    255.416667\n",
              "A98E8M4QLI9RS      35.400000\n",
              "AMPMTF5IAAMK8      63.316667\n",
              "ANO5I7E78QMEN     103.366667\n",
              "AVBRJBJONL47I      24.966667\n",
              "AY7WPVKHVNBLG     237.166667\n",
              "Name: WorkDuration, dtype: float64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>WorkDuration</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>WorkerId</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>A1CY7IOJ9YH136</th>\n",
              "      <td>14.016667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A2C84POENS2UNY</th>\n",
              "      <td>255.416667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A98E8M4QLI9RS</th>\n",
              "      <td>35.400000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AMPMTF5IAAMK8</th>\n",
              "      <td>63.316667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ANO5I7E78QMEN</th>\n",
              "      <td>103.366667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AVBRJBJONL47I</th>\n",
              "      <td>24.966667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AY7WPVKHVNBLG</th>\n",
              "      <td>237.166667</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> float64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7KDMeRSp_RtU"
      },
      "source": [
        "6. **[10 points]** As we talked about in class workers can use tools to accept batches of HITs at once and then work on them sequentially. We suspect some of the workers in this batch have been using such a tool and that their work times overestimate how long they actually spent working. Write a method to calculate how long each worker actually spent working."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8h_wVppv_8dO"
      },
      "source": [
        "Hint: try to think about a worker's accept and submit times would look like if they were doing this and any overlap you might be able to find."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i140DAOe7Q6W"
      },
      "source": [
        "def calculated_work_time(df):\n",
        "    df_sorted = df.sort_values(['WorkerId', 'AcceptTime'])\n",
        "\n",
        "    result = {}\n",
        "\n",
        "    for worker_id in df_sorted['WorkerId'].unique():\n",
        "        worker_data = df_sorted[df_sorted['WorkerId'] == worker_id].copy()\n",
        "\n",
        "        if len(worker_data) == 1:\n",
        "            result[worker_id] = worker_data['SubmitTime'].iloc[0]\n",
        "            - worker_data['AcceptTime'].iloc[0]\n",
        "        else:\n",
        "            total_time = 0\n",
        "            current_accept = None\n",
        "            current_submit = None\n",
        "\n",
        "            for _, row in worker_data.iterrows():\n",
        "                accept_time = row['AcceptTime']\n",
        "                submit_time = row['SubmitTime']\n",
        "\n",
        "                if current_accept is None:\n",
        "                    current_accept = accept_time\n",
        "                    current_submit = submit_time\n",
        "                else:\n",
        "                    if accept_time <= current_submit:\n",
        "                        current_submit = max(current_submit, submit_time)\n",
        "                    else:\n",
        "                        total_time += current_submit - current_accept\n",
        "                        current_accept = accept_time\n",
        "                        current_submit = submit_time\n",
        "\n",
        "            total_time += current_submit - current_accept\n",
        "            result[worker_id] = total_time\n",
        "\n",
        "    return pd.Series(result)"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cfpPd9wuYx93",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "outputId": "3eed3b3b-4055-4823-a2c1-c8dd497ea034"
      },
      "source": [
        "# EXAMPLE\n",
        "calculated_work_time(df)\n",
        "# Series should look the same as above but with different values for some workers"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "A1CY7IOJ9YH136     14.016667\n",
              "A2C84POENS2UNY     58.550000\n",
              "A98E8M4QLI9RS      35.400000\n",
              "AMPMTF5IAAMK8      63.316667\n",
              "ANO5I7E78QMEN     103.366667\n",
              "AVBRJBJONL47I      24.966667\n",
              "AY7WPVKHVNBLG      45.866667\n",
              "dtype: float64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>A1CY7IOJ9YH136</th>\n",
              "      <td>14.016667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A2C84POENS2UNY</th>\n",
              "      <td>58.550000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>A98E8M4QLI9RS</th>\n",
              "      <td>35.400000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AMPMTF5IAAMK8</th>\n",
              "      <td>63.316667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>ANO5I7E78QMEN</th>\n",
              "      <td>103.366667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AVBRJBJONL47I</th>\n",
              "      <td>24.966667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AY7WPVKHVNBLG</th>\n",
              "      <td>45.866667</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> float64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QauDcvD8DGfN"
      },
      "source": [
        "7. **[0 points]** Here we'll show you how you can plot the data you just looked at.\n",
        "\n",
        "Comment all of this out before you submit."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HQtCynncEWlS"
      },
      "source": [
        "#plot_df = pd.DataFrame()"
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uk91lSRnCP9d"
      },
      "source": [
        "#plot_df['WorkTime'] = get_work_time(df)"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o3hUNeWqDR09"
      },
      "source": [
        "#plot_df['CWorkTime'] = calculated_work_time(df)"
      ],
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XhEuWPYJDnpt",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 583
        },
        "outputId": "61d5f489-a4ca-4a5d-a342-5a0a3f51507e"
      },
      "source": [
        "#plot_df.plot(kind='bar')"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='WorkerId'>"
            ]
          },
          "metadata": {},
          "execution_count": 21
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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F52R7Obmhl27dr3wcSpUqIDNmzfr8tRERESkR3g1YyIiIlIcFhQiemP5+vq+0tWOJ02ahLp165ZYHiIqPl7NmKismGRdys+X8lJflpSUhGnTpmHTpk24efMmHB0dUbduXYwYMQJLly5FcnKy1mUztm7divbt22PixImYNGnS/3/6SZMQGhqK+Pj4V/1OCuXh4YHr168Xub5///74+eef8emnn76W5yei52NBIaISc+3aNTRr1gw2NjaYPXs2ateujZycHPzzzz8IDg7GF198gS+//BK5ubkwMHj89hMVFQU3NzdER0drPVZUVBT8/PxeKkd2dvYLr+t1+PBh5OXlAQD279+PHj164MKFC9I8S6amprCwsICFhcVLZSCiV8NDPERUYoYNGwaVSoVDhw6hR48e8PLyQs2aNTFy5EgcOHAAfn5+SE9Px5EjR6SviY6Oxrhx43Dw4EFkZmYCeHwtmoMHD0oFJT4+Hl27doWFhQWsrKzw4Ycfak34+ORQzLJly557/ZpNmzbB2toav//+OxwcHODs7AxnZ2fY2dkBABwdHaVl1tbWBQ7xDBgwAN26dcP06dPh5OQEGxsbTJkyBbm5uRg9ejTs7OxQvnx5hIWFaT1vQkICPvzwQ9jY2MDOzg5du3bFtWvXSuIlJ3pjsaAQUYm4f/8+tm7diuDg4EKvKGxjYwMvLy+4uroiKioKAJCWloajR4/igw8+gIeHB2JiYgA83qORlZUFPz8/5Ofno2vXrrh//z527dqFbdu24erVq+jZs6fW41++fBnr1q3D+vXrtS5G+sSKFSvQu3dv/P777wgICHjp73Pnzp24desWdu/ejblz52LixIno1KkTbG1tcfDgQXzyyScYMmQIbty4AQDIycmBv78/LC0tsWfPHuzbtw8WFhZo164dsrOzXzoH0ZuOBYWISsTly5chhEC1atWeu52fn590OGfPnj3w8vKCg4MDWrZsKS2Pjo5GxYoVUaFCBezYsQOnTp3CihUr0KBBA3h7e2P58uXYtWsXDh8+LD1udnY2li9fjnr16kkTQz6xYMECDBs2DJGRkejUqdMrfZ92dnaYN28eqlatisDAQFStWhUPHz7EV199hSpVqmD8+PEwMjKSrlO2evVq5OfnY9myZahduzaqV6+OsLAwxMfHFzisRUT/H8egEFGJeNE8SU88ObMmJycH0dHR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2rQpmjRpAgBo27YtatSogb59+2LWrFlISkrCN998g+DgYBgbG5f8d0hERERljk4FZdGiRQAAX19freVhYWEYMGAAAOCHH36AWq1Gjx49kJWVBX9/fyxcuFDaVqPRYOPGjRg6dCiaNm0Kc3Nz9O/fH1OmTHm174SIiIjeGDoVlOJMmWJiYoIFCxZgwYIFRW5ToUIFbN68WZenJiIiIj3Ca/EQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4uhcUHbv3o3OnTvD1dUVKpUKf/75p9b6AQMGQKVSad3atWuntc39+/cREBAAKysr2NjYICgoCOnp6a/0jRAREdGbQ+eCkpGRgTp16mDBggVFbtOuXTskJiZKt5UrV2qtDwgIwJkzZ7Bt2zZs3LgRu3fvxscff6x7eiIiInojGej6Be3bt0f79u2fu42xsTGcnZ0LXXfu3Dls3boVhw8fRsOGDQEA8+fPR4cOHTBnzhy4urrqGomIiIjeMK9lDEp0dDQcHR1RtWpVDB06FP/995+0LiYmBjY2NlI5AYDWrVtDrVbj4MGDryMOERERlTE670F5kXbt2qF79+6oWLEirly5gq+++grt27dHTEwMNBoNkpKS4OjoqB3CwAB2dnZISkoq9DGzsrKQlZUl3U9NTS3p2ERERKQgJV5QevXqJf137dq18fbbb6Ny5cqIjo5Gq1atXuoxZ8yYgcmTJ5dURCIiIlK4136acaVKlfDWW2/h8uXLAABnZ2fcuXNHa5vc3Fzcv3+/yHEr48ePR0pKinRLSEh43bGJiIhIRq+9oNy4cQP//fcfXFxcAABNmzZFcnIyYmNjpW127tyJ/Px8eHt7F/oYxsbGsLKy0roRERHRm0vnQzzp6enS3hAAiIuLw/Hjx2FnZwc7OztMnjwZPXr0gLOzM65cuYIxY8bA09MT/v7+AIDq1aujXbt2GDx4MBYvXoycnBwMHz4cvXr14hk8REREBOAl9qAcOXIE9erVQ7169QAAI0eORL169TBhwgRoNBqcPHkSXbp0gZeXF4KCgtCgQQPs2bMHxsbG0mP8/vvvqFatGlq1aoUOHTqgefPm+OWXX0ruuyIiIqIyTec9KL6+vhBCFLn+n3/+eeFj2NnZYcWKFbo+NREREekJXouHiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFIcFhYiIiBSHBYWIiIgUhwWFiIiIFMdA1y/YvXs3Zs+ejdjYWCQmJmLDhg3o1q2btF4IgYkTJ2Lp0qVITk5Gs2bNsGjRIlSpUkXa5v79+/j0008RGRkJtVqNHj164KeffoKFhUWJfFNERErjMW5TiTzONZOPSuRxMCmlZB6H6DXReQ9KRkYG6tSpgwULFhS6ftasWZg3bx4WL16MgwcPwtzcHP7+/sjMzJS2CQgIwJkzZ7Bt2zZs3LgRu3fvxscff/zy3wURERG9UXTeg9K+fXu0b9++0HVCCPz444/45ptv0LVrVwDA8uXL4eTkhD///BO9evXCuXPnsHXrVhw+fBgNGzYEAMyfPx8dOnTAnDlz4Orq+grfDhEREb0JSnQMSlxcHJKSktC6dWtpmbW1Nby9vRETEwMAiImJgY2NjVROAKB169ZQq9U4ePBgScYhIiKiMkrnPSjPk5SUBABwcnLSWu7k5CStS0pKgqOjo3YIAwPY2dlJ2zwrKysLWVlZ0v3U1NSSjE1EREQKUybO4pkxYwasra2lm5ubm9yRiIiI6DUq0YLi7OwMALh9+7bW8tu3b0vrnJ2dcefOHa31ubm5uH//vrTNs8aPH4+UlBTplpCQUJKxiYiISGFKtKBUrFgRzs7O2LFjh7QsNTUVBw8eRNOmTQEATZs2RXJyMmJjY6Vtdu7cifz8fHh7exf6uMbGxrCystK6ERER0ZtL5zEo6enpuHz5snQ/Li4Ox48fh52dHdzd3TFixAhMnToVVapUQcWKFfHtt9/C1dVVmiulevXqaNeuHQYPHozFixcjJycHw4cPR69evXgGDxEREQF4iYJy5MgR+Pn5SfdHjhwJAOjfvz/Cw8MxZswYZGRk4OOPP0ZycjKaN2+OrVu3wsTERPqa33//HcOHD0erVq2kidrmzZtXAt8OERERvQl0Lii+vr4QQhS5XqVSYcqUKZgyZUqR29jZ2WHFihW6PjURERHpiTJxFg8RERHpFxYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwWFCIiIlIcFhQiIiJSHBYUIiIiUhwDuQMQ0ZvDY9ymEnmcayYflcjjYFJKyTwOEZU67kEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLF4WnG9HpNsi6hx+HpokRE+oR7UIiIiEhxWFCIiIhIcVhQiIiISHFYUIiIiEhxWFCIiIhIcVhQiIiISHFKvKBMmjQJKpVK61atWjVpfWZmJoKDg2Fvbw8LCwv06NEDt2/fLukYREREVIa9lj0oNWvWRGJionTbu3evtO6LL75AZGQk1q5di127duHWrVvo3r3764hBREREZdRrmajNwMAAzs7OBZanpKQgJCQEK1aswLvvvgsACAsLQ/Xq1XHgwAE0adLkdcQhIiKiMua17EG5dOkSXF1dUalSJQQEBCA+Ph4AEBsbi5ycHLRu3Vratlq1anB3d0dMTEyRj5eVlYXU1FStGxEREb25SrygeHt7Izw8HFu3bsWiRYsQFxeHFi1aIC0tDUlJSTAyMoKNjY3W1zg5OSEpKanIx5wxYwasra2lm5ubW0nHJiIiIgUp8UM87du3l/777bffhre3NypUqIA1a9bA1NT0pR5z/PjxGDlypHQ/NTWVJYWIiOgN9tpPM7axsYGXlxcuX74MZ2dnZGdnIzk5WWub27dvFzpm5QljY2NYWVlp3YiIiOjN9doLSnp6Oq5cuQIXFxc0aNAAhoaG2LFjh7T+woULiI+PR9OmTV93FCIiIiojSvwQz5dffonOnTujQoUKuHXrFiZOnAiNRoPevXvD2toaQUFBGDlyJOzs7GBlZYVPP/0UTZs25Rk8REREJCnxgnLjxg307t0b//33HxwcHNC8eXMcOHAADg4OAIAffvgBarUaPXr0QFZWFvz9/bFw4cKSjkFERERlWIkXlFWrVj13vYmJCRYsWIAFCxaU9FMTERFRYSZZl8BjpLz6Y+iA1+IhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsUxkDsAUVnkMW7TKz/GNZOPSiAJSv0S6EREpYF7UIiIiEhxWFCIiIhIcVhQiIiISHFYUIiIiEhxWFCIiIhIcVhQiIiISHFYUIiIiEhxWFCIiIhIcVhQiIiISHFYUIiIiEhxWFCIiIhIcVhQiIiISHFYUIiIiEhxeDVjIiKSVUlcHRzgFcLfNNyDQkRERIrDgkJERESKw4JCREREisOCQkRERIrDgkJERESKw4JCREREisOCQkRERIrDgkJERESKw4JCREREisOCQkRERIrDgkJERESKw4JCREREisOCQkRERIrDgkJERESKYyB3ALkp6jLfvMQ3ERERAO5BISIiIgViQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFkbWgLFiwAB4eHjAxMYG3tzcOHTokZxwiIiJSCNkKyurVqzFy5EhMnDgRR48eRZ06deDv7487d+7IFYmIiIgUQraCMnfuXAwePBgDBw5EjRo1sHjxYpiZmSE0NFSuSERERKQQBnI8aXZ2NmJjYzF+/HhpmVqtRuvWrRETE1Ng+6ysLGRlZUn3U1JSAACpqamvnCU/6+ErPwYApKpECTzIq38/JakkXpsSeV0AvjbPfSDlvDaK+n0C+No894H42hT9QHxtCn+QV39dnnxuC1GMPEIGN2/eFADE/v37tZaPHj1aNG7cuMD2EydOFAB444033njjjbc34JaQkPDCriDLHhRdjR8/HiNHjpTu5+fn4/79+7C3t4dKpZIx2WOpqalwc3NDQkICrKys5I6jGHxdisbXpmh8bYrG16ZofG2KpqTXRgiBtLQ0uLq6vnBbWQrKW2+9BY1Gg9u3b2stv337NpydnQtsb2xsDGNjY61lNjY2rzPiS7GyspL9f74S8XUpGl+bovG1KRpfm6LxtSmaUl4ba2vrYm0nyyBZIyMjNGjQADt27JCW5efnY8eOHWjatKkckYiIiEhBZDvEM3LkSPTv3x8NGzZE48aN8eOPPyIjIwMDBw6UKxIREREphGwFpWfPnrh79y4mTJiApKQk1K1bF1u3boWTk5NckV6asbExJk6cWOAwlL7j61I0vjZF42tTNL42ReNrU7Sy+tqohCjOuT5EREREpYfX4iEiIiLFYUEhIiIixWFBISIiIsVhQSEiIiLFYUEhIiIixWFBKQG5ublyR5DVrVu35I5ARERvGJ5mrIOtW7eiXLlyqF27NvLz8zFt2jQsXrwYSUlJcHFxwfDhwzF27FhFXB+oNNna2mLBggX46KOP5I6iSPfu3UNGRgYqVKggLTtz5gzmzJmDjIwMdOvWTW9fu7y8PFy/fh0eHh5Qq9XIysrCX3/9hfz8fPj5+ZXJeZFKyu7du4u1XcuWLV9zEmU5efJksbZ7++23X3MSZUpNTZWms9+8ebPWH9AajQYdO3aUK5ruSuLqxPqiatWqYvfu3UIIIaZPny7s7e3F3LlzxZYtW8SPP/4onJycxMyZM2VOWfoWLFggLCwsxPvvvy/+++8/ueMoTq9evcTIkSOl+7dv3xa2traiZs2aokuXLsLQ0FAsX75cxoTyOHHihHBxcRFqtVrUqlVLxMfHi1q1aglzc3NhYWEhbG1txaFDh+SOKRuVSlXkTa1WC7VaLTQajdwxS92T77+o1+XJv/ooMjJS1K1bV7pvYWFR4PVZu3atjAl1w4KiA2NjY3H9+nUhhBC1atUSa9as0Vq/ceNG4enpKUc02V29elX4+fkJJycn8ffff8sdR1E8PDxEdHS0dH/27NmicuXKIicnR7rv7e0tVzzZ+Pv7i/fff1+cOnVKfP7556J69erigw8+ENnZ2SInJ0f06dNHtG7dWu6YsklOTi70duvWLTF27FhhamoqatasKXfMUnft2rVi3fRR586dRUhIiHTfwsJCXLlyRbr//fffi/bt28sR7aWwoOjAxcVFxMTECCGEcHJyEkePHtVaf/HiRWFqaipHNMWYP3++MDAwELVr1xb16tXTuukrExMTrTfM9u3bi9GjR0v3L1y4IOzs7OSIJitbW1tx9uxZIYQQDx8+FBqNRhw8eFBaf/r0aWFvby9XPMXJy8sTS5cuFeXLlxfu7u4iNDRU5OXlyR2LFMTDw0OcP39euv9sQTl58qRwcHCQI9pLke1aPGXRe++9h2nTpuHPP/9E165dsXDhQvzyyy/SmJP58+ejbt268oaU0fXr17F+/XrY2tqia9euMDDgjxfw+BLnycnJ0hiUQ4cOISgoSFqvUqmQlZUlVzzZCCGkn5Fn/wUeHy/Pz8+XJZvSrF+/Hl999RXu3r2L8ePH49NPPy1z11UpKevWrUP79u1hZmYmdxTFSUxM1Pq5iIqKgpubm3TfwsICKSkpckR7OXI3pLIkOTlZNGzYUHh6eoq+ffsKExMTUaFCBdGmTRtRsWJFYW1tLQ4cOCB3TFn88ssvwtLSUrz33nvizp07csdRlC5duojAwECRl5cn1q5dK4yMjMT9+/el9Rs3bhTVqlWTMaE8WrVqJYKCgsSNGzfE5MmThaenpxg4cKC0ftiwYaJFixYyJpRfdHS08Pb2FmZmZmL8+PEiOTlZ7kiyU6lUwsrKSgwePFhv32+L4uLiIrZt21bk+n/++Uc4OzuXYqJXw4Kio+zsbLFo0SLRoUMHUa1aNeHl5SV8fHzEV199JRISEuSOJwt/f39ha2srIiIi5I6iSCdOnBBvvfWWMDIyEmq1WnzzzTda6/v06SOGDBkiUzr5HDp0SNjb2wu1Wi0cHBzE6dOnhbe3t3B2dhaurq7C1NRUbN++Xe6Ysmnfvr0wNDQUQ4YMEYmJiXLHUQyVSiWmTJki6tWrJ1QqlahZs6b44YcfxL179+SOJruePXuKzp07F7m+Y8eO4sMPPyzFRK+GpxnTK2vTpg3CwsJQvnx5uaMo1r1797Bv3z44OzvD29tba92mTZtQo0YNVKxYUaZ08snIyMD58+dRtWpVWFhYIDMzE7///jsePXqENm3aoGrVqnJHlI1arYaBgQHMzc2fO3XB/fv3SzGV/NRqNZKSkuDo6IjY2FiEhIRg5cqVePToEbp06YLBgwejTZs2cseUxbFjx9C0aVN07twZY8aMgZeXFwDgwoUL+P7777Fp0ybs378f9evXlzlp8bCglAAhBPLz86HRaOSOQmXUzZs3Ua5cObljlKpbt27B1dX1udusWrUKvXr1KqVEyhIREVGs7fr37/+akyjL0wXliczMTKxduxahoaHYvXs33N3dERcXJ2NK+fz1118YNGhQgeJqa2uLZcuWoVu3bvIEewksKDrIzc3FpEmTsGfPHvj6+mLy5MmYPXs2Jk2ahNzcXPTq1QtLly6FkZGR3FFLVWBg4Au3UalUCAkJKYU0ZUtSUhKmTZuGkJAQPHz4UO44papWrVrYu3cvbGxsCl2/atUq9OvXD9nZ2aUbjBRNo9EgMTFRq6A87fLlywgLC8O0adNKOZlyPHz4EP/88w8uXboEAKhSpQratm0Lc3NzmZPphlPd62Dy5MlYtmwZGjZsiD/++ANDhw7F/Pnz8csvv2Dp0qXYsWMHfvzxR7ljlroHDx4Uebt37x5WrVqF8PBwuWPK5sGDB+jduzfeeustuLq6Yt68ecjPz8eECRNQqVIlHD58GGFhYXLHLHUODg5o3759ocVszZo16Nu3r15/yBw6dAh5eXlFrs/KysKaNWtKMZEyvOhvak9PT73+uQEAMzMzvPfeexgzZgzGjBmD9957D+bm5rhx4wY+/vhjueMVn3zDX8qeSpUqicjISCGEEJcuXRJqtVqsWrVKWr969WpRq1YtueIpzp9//ilq1KghbGxsxIwZM+SOI5uPP/5YuLu7i1GjRolatWoJtVot2rdvLzp27CjNq6OP0tLSRIMGDUSbNm1Edna2tHzNmjXCyMhIL2dlfpparRa3b9+W7ltaWmrNaZGUlKSXM6Zeu3ZN5Ofnyx2jTDp+/HiZ+plhQdGBiYmJiI+P17p/7tw56f7Vq1eFpaWlHNEUZe/evaJ58+bCzMxMjBkzRuuUWn3k5uYmduzYIYQQIi4uTqhUKjF+/HiZUynDnTt3RLVq1cT7778v8vPzxdq1a4WhoaGYNm2a3NFkp1KptArKs5NuJSUlCZVKJUc0RWJpebGyVlB4iEcH1tbWSE5Olu7Xr18flpaW0v2srCy9u1Dg086ePYvOnTvD19cXXl5e0shxW1tbuaPJ6tatW6hevToAwMPDAyYmJujTp4/MqZTBwcEB//77Lw4dOoQ2bdogICAAEyZMwFdffSV3tDJBn99vnmVsbIxz587JHYNKEKf61EGNGjVw9OhR1K5dGwCwb98+rfWnTp1ClSpV5Igmq4SEBEyYMAG//fYbOnXqhJMnT0ofyKQ9YyrweJCfqampjImU4emr0s6ePRv9+vVDt27d0KVLF611+npVWircyJEjC12el5eHmTNnwt7eHgAwd+7c0oxFrwHP4tHBxYsXYWhoWOR8FStWrICBgQE+/PDDUk4mLzMzM6hUKgwfPhzNmjUrcrsuXbqUYirlUKvVqFWrllRSTp48iWrVqhU42+vo0aNyxJONWq2GSqWCEEL6F0CB/37eQNE3mVqtxs6dO2FnZwcAeOedd7BmzRppvqF79+6hTZs2evf6qNVq1KlTp8DZX7t27ULDhg2leWN27twpT0AZde/e/bnrk5OTsWvXrjLzM8OCQq9MrX7xkUJ9/qCZPHlysbabOHHia06iLNevXy/Wdk+uYaRvni5wz3q62Onb79XMmTPxyy+/YNmyZXj33Xel5YaGhjhx4gRq1KghYzp5DRw4sFjblZWzBllQSlBubi5u3boFd3d3uaMQURnHAle0w4cPo0+fPujcuTNmzJgBQ0NDFpQ3EMeglKAzZ86gfv36evcXDRVfXl4e7t27B7VaDQcHB7njyCo+Pr5Y2+lr4dfH4lFcjRo1QmxsLIKDg9GwYUP8/vvvHDD8BmJBoVc2b968QpdbW1vDy8sLTZs2LeVEyrNp0yZ8//33OHToEHJycgAAlpaW6Ny5M6ZNm6aXH8JPj+V6eszJ08v08RDGEyxwz2dhYYGIiAisWrUKrVu31tufk2dFRUXh6NGjaNKkCZo1a4YlS5Zg2rRpePToEbp164Z58+aVmUH6PMSjgxddYOnRo0e4ePGi3v2iFDVoODk5GSkpKXjnnXfw999/S4P99M2vv/6K4OBgfPzxxzAxMUFISAgGDBiAChUqYNWqVThz5gz279+vd2eAGRgYoHz58hgwYAA6d+6sdabT0+rUqVPKyZTh6Wt7scA9340bNxAbG4vWrVuXuencS9LSpUsxdOhQVKxYEQkJCZg4cSKmTZuGvn37Qq1W47fffsPQoUMxc+ZMuaMWCwuKDkxMTNCrV68iP5ATExOxdOlSvmE85erVq+jTpw/q1q2LhQsXyh1HFtWrV8ekSZPQs2dPAMCRI0fw3nvvIT4+HiqVCr169UJ2djbWr18vc9LSlZSUhIiICISFhSE5ORl9+vRBUFAQT1H/PyxwL+f8+fPo0qULLl68KHeUUlerVi0MGTIEn376KbZu3YrOnTtj2bJl0gUl165di/Hjx+Py5csyJy2m0p0Xrmxr0KCBWLhwYZHrjx07VqZm6Sstu3btEpUrV5Y7hmxMTU1FXFyc1jIDAwNx8+ZNIYQQBw8eFDY2NjIkU449e/aIwMBAYWlpKby9vcUvv/wi8vLy5I4lq8TERDFz5kxRtWpV4eTkJEaNGiXOnj0rdyzFK2uzpZYkU1NTce3aNem+oaGh1s/M9evXhZGRkRzRXgpnktVBs2bNcOHChSLXW1paomXLlqWYqGxwd3dHUlKS3DFk4+HhgSNHjkj3jx49CrVaDScnJwCAnZ2dNC5FXzVv3hwhISG4dOkSzMzM8Mknn2jN2qyPnJ2dMXbsWJw/fx5//PEHHjx4AG9vbzRp0gRLly5Ffn6+3BFJYTIzM7XGlxgbG8PY2Fjrfm5urhzRXgoHyergp59+eu76ypUrIyoqqpTSlB2nTp3S6zMSgoODMWjQIBw+fBgmJiZYtmwZ+vbtK40xOHjwILy8vGROKa/9+/cjNDQUa9euRdWqVbFgwYICE3Hps+bNm6N58+aYPn06evfujU8++QQ9evTQ23FdVDiVSoW0tDSYmJhIY5TS09ORmpoKANK/ZQULCr2yon7oU1JSEBsbi1GjRknHQPVRcHCwNEAtKysLAwYMwLfffiutb9y4MVasWCFjQnkkJiZi+fLlCAsLw4MHDxAQEIB9+/ahVq1ackdTHBY4Kg4hhNYfO0II1KtXT+t+WTodm4NkdfD09UGeR9+uHfJkxsvCqFQqDBo0CPPmzSswtTvpN0NDQ5QrVw79+/dHly5dYGhoWOh2+vb79ERhBS4wMFDvC5ytre1zP2Rzc3ORkZGhlycr7Nq1q1jb+fj4vOYkJYMFRQfPTj395JdEPHUtEX087a+oXworKytUqVIFFhYWpZyIyoKnL5Hw9O/S0/Tx9+kJFrjCRUREFGs7fd5r+6ZgQdHB01NPCyFQq1YtbN68ucD4Cn0eb0EFvegvvifu379fCmmUg1O5Px8LHOk7jkHRwbNvlCqVCuXLl9fbN9Bn5efnF3rhwPz8fNy4cUNvZ7z88ccf5Y6gSMX5vTl9+nQpJFGmuLg4uSNQGfO8w+1PqFSqMnMmD/egvAJLS0ucOHEClSpVkjuKrFJTUzFo0CBERkbCysoKQ4YMwcSJE6WzVG7fvg1XV1f+pVeE3Nxc3LlzB66urnJHUYS0tDSsXLkSy5YtQ2xsLH9uSEvFihWL9SF85cqVUkqkHH/99VeR62JiYjBv3jzk5+cjMzOzFFO9PO5BoVf27bff4sSJE/j111+RnJyMqVOn4ujRo1i/fr00MJY9uGi8yORju3fvRkhICNatWwdXV1d0794dCxYskDuW7A4fPoyVK1fi4sWLMDIyQtWqVdG3b1+9vWrviBEjilx37do1LFmyBFlZWaUXSEG6du1aYNmFCxcwbtw4REZGIiAgAFOmTJEh2Usq5Ynh3igWFhbi6tWrcseQnbu7u4iKipLu3717VzRu3Fi0bdtWZGZmiqSkJL2d2bE49Hnmy8TERDFjxgzh6ekpHB0dxfDhw4WBgYE4c+aM3NEUYfTo0UKlUglLS0tRp04dUadOHWFhYSE0Go2YOXOmEEKIR48eiZ07d8qcVF7//fefGDFihDA2NhYtW7YUMTExckeS3c2bN8WgQYOEoaGh6NSpkzh16pTckXTGPSg6qFevntauxUePHqFz584FTp89evRoaUeT1d27d7XGE7z11lvYvn07/P390aFDByxbtkzGdKRUnTt3xu7du9GxY0f8+OOPaNeuHTQaDRYvXix3NEWIiIjA/PnzMW/ePAwZMkQ6iycnJweLFi3CuHHjULFiRSxatAitWrWCn5+fzIlL36NHjzB37lzMmTMHFSpUwPr169GhQwe5Y8kqJSUF06dPx/z581G3bl3s2LEDLVq0kDvWS2FB0UHXrl21Ckphu9P0kbu7O86dO6d1EUVLS0v8+++/aNu2Ld577z0Z05FSbdmyBZ999hmGDh2qd1dyLo4FCxZg+vTpGD58uNZyQ0NDfPbZZ8jNzUXv3r1Rt25dBAcHy5RSHnl5eVi6dCkmT54MExMTzJs3D3369ClTk5C9DrNmzcL3338PZ2dnrFy5ssx/RnGQrA5EGZuFr7R89tlnSExMxNq1awusS0tLQ5s2bXD48GG9HWPxogn+zp8/j969e+vd63PgwAGEhIRg9erVqF69Ovr27YtevXrBxcUFJ06c0NsxFk+Ym5vj1KlTRQ7Cv3r1Kjw9PXH//n29mlV2zZo1+Oabb5CcnIyvv/4aQ4cO5SSQ/0etVsPU1BStW7eWTlIoTFm5cjoLig7eeecdLF++HJ6ennJHUZQHDx7g1q1bqFmzZqHr09LScPTo0TIze2FJe3aCv6fp8wR/T2RkZGD16tUIDQ3FoUOHkJeXh7lz5yIwMBCWlpZyx5ONlZUVDh06hGrVqhW6/sKFC2jUqFGZu77Kq3ryIdy7d29YWVkVud3cuXNLMZUyDBgwoFh/RIeFhZVCmlfHgqKDDz/8EJs3b8b333+vd7tU6eVxQrLiu3DhAkJCQqQzwtq0aYO///5b7liy8PX1RYsWLfDdd98Vuv6bb77B3r17ER0dXbrBZObr61us04x37txZSonotZFteG4ZtWbNGuHo6Chat24tEhIS5I6jCPv37xeRkZFayyIiIoSHh4dwcHAQgwcPFpmZmTKlo7IoNzdXbNiwQXTu3FnuKLKJjIwUGo1GjB49WiQlJUnLExMTxZdffikMDAzE33//LWNCUpoePXqILVu2iPz8fLmjlAjuQXkJd+/eRXBwMLZt24a+ffvCwEB7rLG+7Vps3749fH19MXbsWADAqVOnUL9+fQwYMADVq1fH7NmzMWTIEEyaNEneoDLjfBa6yc/Px+bNm9GpUye5o8hm/vz5+PLLL5Gbmwtra2sAj8/S0Gg0mDVr1nPnBNEX9+7dA/D47EF916pVK0RHR8PV1RUDBw7EgAEDyvREoiwoLyEvLw9TpkzB9OnT0aRJE62Coo+7Fl1cXBAZGYmGDRsCAL7++mvs2rULe/fuBQCsXbsWEydOxNmzZ+WMKasxY8Zgzpw5sLCwkN4wrly5gkePHmHatGkYO3YsMjMzERMTo5eniz7t8uXLCA0NRXh4OO7evYucnBy5I8nqxo0bWLt2LS5dugQAqFKlCt5//324ubnJnEw+TwbIrl69Gg8ePADw+JpXvXr1wtSpU/Vq0PCzrl+/jrCwMCxfvhzXr1+Hj48PBg0ahB49esDY2FjueLqRdwdO2XP69GlRv3594eHhofeTIz1hbGws4uPjpfvNmjUTU6dOle7HxcUJCwsLOaIpQnh4uDAxMRHz588X2dnZ0vLs7Gzx008/CVNTU7F69Wrh6+srvvvuOxmTyufhw4ciIiJCtGjRQqjVauHj4yMWLVqkdWiDSIjHk7J5eXkJc3Nz8fHHH4sffvhB/PDDD2Lw4MHC3NxcVKtWTdy/f1/umIqwY8cOERAQIMzMzIStra0YNmyYOHLkiNyxio0FRQczZswQxsbGYuDAgSI1NVXuOIrh7u4udu3aJYQQIisrS5iamort27dL60+ePClsbW3liie7Ro0aiblz5xa5/n//+59Qq9Wifv36evfGeujQIfHxxx8LKysrUa9ePTFnzhyh0Wg4k+z/OX78uAgJCZFmrD59+rQYOnSoGDJkiNi6davM6eTx+eefi1q1ahVaXhMTE0Xt2rXFiBEjZEimXKmpqWLx4sXCzs5OaDQaueMUGwuKDpydnTkorRCffPKJaNq0qdi9e7cYOXKksLe3F1lZWdL63377TTRs2FDGhPIyMzMTV65cKXL9lStXhEqlEg8ePCi9UApQu3ZtUaFCBTF+/Hhx+vRpaTmnun9s3bp1QqPRCHt7e2FhYSG2bdsmbGxsROvWrYW/v7/QaDTi999/lztmqatQocJzy9mWLVtEhQoVSi+Qwl29elVMmDBBuLu7C41GI/z9/eWOVGwsKDq4d++e3BEU6e7du6JFixbSNUPWr1+vtf7dd98VX331lUzp5GdpaSnOnTtX5Prz588LS0vLUkykDEZGRqJv377i33//1TrrgAXlsfr160uHSleuXClsbGzElClTpPVz5swRdevWlSuebIyMjJ57BmVCQoIwNjYuxUTK8+jRI/Hrr78KPz8/odFohIeHh5g8ebLWofiygINkdfTo0SOsXLkSe/fuRWJiItRqNSpVqoRu3bqhVatWcseTVUpKCiwsLArMYHj//n1YWFjo7WyPnM+icDdv3kR4eDjCwsLw6NEj9O7dGwEBAfD29sbx48f1/uwmCwsLnD59Gh4eHhBCwNjYGLGxsahduzaAxzPJ1qlTB2lpaTInLV3lypXD6tWr0bx580LX79mzBz179sStW7dKOZn8Dh06hNDQUKxevRqZmZl47733EBgYiFatWpXNWdBlLkhlyqVLl0SFChWEo6OjcHNzEyqVSnTs2FF4e3sLjUYjPvjgA5GTkyN3TFIYzmfxYk8G85mamgqVSiVGjx4tLly4IHcsWTk7O0sDGu/fvy9UKpXWVcMPHToknJ2dZUonn4EDB4qWLVtqHUZ+IjMzU/j4+IiBAwfKkEx+KpVK1K1bV8yfP/+NGM/GPSg66NChA9zd3bFo0SKoVCp8//332LVrFzZv3oxLly6hbdu26N+/v97N9xEYGPjCbVQqFUJCQkohjTJxPoviSUlJwe+//47Q0FAcPXoUtWrVeuG1jN5Uffv2xaVLl/Dpp59i9erVyM7ORkpKCsLCwqBSqTBkyBA4ODgUeg2sN9mNGzfQsGFDGBsbIzg4GNWqVYMQAufOncPChQuRlZWFI0eO6OVp2EePHkX9+vXljlFiWFB0YG5ujuPHj0tXXs3OzoaFhQUSExNhb2+Pv/76CyNGjEBcXJzMSUvX865WnJeXh+3btyMrK0tvrzXzBOez0M3x48cRGhqKefPmyR1FFrdv30bfvn0RExODZs2aYfXq1fjmm2+wYMECqFQqVK5cGVu2bEHlypXljlrq4uLiMGzYMPz777/SNa5UKhXatGmDn3/+WW+vl1bcMv/222+/5iQlgwVFB+XKlUNkZKTUUJOTk2FnZ4eUlBRYWloiLi4O1atXR2ZmpsxJleGvv/7CV199hVu3bmHs2LEYN26c3JGIyryrV6/i4cOHqFatWoFZrPXNgwcPpMLv6ekJOzs7mRPJ69kLkz4ZdyL+74KkooxdmFS/f7p11KZNG4wcORKLFy+GsbExxo8fj7p160pXXI2Pj4ejo6PMKeW3b98+jBs3DkePHsXw4cMxbtw42Nrayh1LcSpVqoR//vlH2iOnb+rVq1esi77FxsaWUqKyoSxPXV7SbG1t0bhxY7ljKMbTe++FEKhVqxY2b95cZi9EyoKig1mzZqFr166oUaMGVCoV3NzcsGHDBmn93bt3MXr0aBkTyuvs2bMYO3Ystm7din79+mHlypUoX7683LFkV9Qhivj4eISFhcHZ2RkA8Nlnn5VmLNl169ZN7giK9umnn+LDDz9EixYt5I6iKN27d3/hNgYGBnB2dkabNm3QuXPnUkilDM8WEZVKhfLly5fZgsJDPC/h0qVLyMrK4i7W/5OQkIAJEybgt99+Q6dOnTB9+nRUr15d7liKoVarUa5cuQI/K9evX4erqysMDQ2hUqlw9epVmRKSEj3ZXV+5cmUEBQWhf//+UpnVZwMHDnzhNvn5+bhz5w527dqFL7/8ElOmTCmFZMpjaWmJEydOlNm9biwo9MrMzMygUqkwfPhwNGvWrMjtunTpUoqplOOTTz7BwYMHsWLFCq3iZmhoiBMnTuj9fB9UOLVajW3btiEyMhK///47UlJS0L59ewwePBgdOnSAWq2WO6Libdy4EcOGDUN8fLzcUWTBgqJHRo4c+cJtnuxabNWqFerUqVMKqeRXnDfKsjQw63XYsGEDPv/8c4wZMwbDhw8HwIJy6NAhNGjQQJrYb+PGjZg9ezYuX74MFxcXfPbZZ+jXr5/MKeWjVquRlJQER0dH5OTkYMOGDQgNDcX27dvh5OSEAQMGYODAgXp7xkpxJCcnIzAwEOvXr5c7iiwsLS1x8uRJVKxYUe4oL4UFRQd+fn4v3ObJrsWLFy9i/vz5GDZsWCkko7Lg5s2b6NevH4yMjBAWFgY3Nze9LigajQaJiYlwdHREZGQkunXrhj59+sDb2xvHjh1DeHg41qxZ89zT2N9kTxeUp8XHxyM0NBTh4eFISEjQy+IfFRWFo0ePokmTJmjWrBmWLFmCadOm4dGjR+jWrRvmzZsHU1NTuWOWumcHnp88eRLVqlUrMIv30aNHSzvaS2FBeU0iIiIwZcoUXLlyRe4opCBCCMycORPz5s3D3bt3cfLkSb0tKE9/ALdo0QLNmzfHjBkzpPXTp09HZGQkYmJiZEwpn6IKyhNCCGzfvh1t2rQp5WTyWrp0KYYOHYqKFSsiISEBEydOxLRp09C3b1+o1Wr89ttvGDp0KGbOnCl31FI3adKkYk1pP3HixFJIUwJKb9LaN8/du3fF3bt3C113584dUb9+/VJOJI+hQ4eKtLQ06f6KFStEenq6dP/Bgweiffv2ckRTrCNHjogff/zxjZiO+mWpVCpx+/ZtIYQQjo6O0rTuT5w/f17Y2NjIEU0RPDw8eIHSQtSsWVPMmzdPCPH4ysUGBgYiPDxcWr9mzRpRuXJlueIp3q1bt+SOUGwcZaWj5ORkBAcH46233oKTkxOcnJzw1ltvYfjw4UhOTpa2c3Bw0Jv5G5YsWYKHDx9K94cMGYLbt29L97OysvDPP//IEU2xGjRogM8//1zv54c5e/YsTp48CVNTU+Tn5xdYn5ubK0MqZYiLi4O9vb3cMRTn6tWr0oD7du3aQaVSac2F4u3tjYSEBLniyepF4yQTExPh6+tbOmFKAM+R1cH9+/fRtGlT3Lx5EwEBAdIZGWfPnkV4eDh27NiB/fv3692HjnjmKOGz9/VdcU9xnDBhwmtOojytWrWSfl727duHRo0aSeuOHTsGd3d3uaIpnhACd+/e1bvJITMzM7XGlxgbG8PY2Fjrvr4W27CwMNjb2+Prr78usO5JOXFwcJAh2cthQdHBlClTYGRkhCtXrsDJyanAurZt22LKlCn44YcfZEpISjRp0iS4urrC0dGxyPKmUqn0rqA8e80qCwsLrfvZ2dkYO3ZsaUZSFDMzM1y/fl36QOnYsSOWLVsGFxcXAMCdO3fg6uqqd4NkVSoV0tLSYGJiIk3dnp6ejtTUVACQ/tVHf//9N9q1awc7OzsMHTpUWp6UlAQ/Pz/Y2dlh69atMibUkZzHl8qaChUqiK1btxa5fsuWLaJChQqlF0ghnh5LIIQQFhYW4sqVK9L9pKQkoVar5YimCB06dBAmJiaia9eu4q+//hJ5eXlyR6IyoDi/VyqVSo5oslKpVEKtVku3ou7rq40bNwpjY2OxcuVKIYQQiYmJolq1aqJx48YiNTVV5nS64R4UHSQmJqJmzZpFrq9VqxaSkpJKMZFyTJgwAWZmZgAe/+U7bdo0WFtbA4DW+BR9tGnTJty6dQsREREYPXo0hgwZgn79+iEwMBBVq1aVO55sJkyYgHHjxkk/Nw8ePNC7w6OvqjhnbLxpoqKi5I6gaB07dkRoaCgGDhyIzMxMzJo1CxYWFvj333+l68aVFTzNWAflypXD6tWr0bx580LX79mzBz179sStW7dKOZm8fH19i/VGyTeWx3bv3o2wsDCsW7cOtWvXxvbt2/Vyzoan50EBACsrKxw/frzMznpZ0p49zfjZWUFv376tl4d4qHgWLlyITz/9FPXr18f27dulPxjLEu5B0YG/vz++/vprbNu2rcDEN1lZWfj222/Rrl07mdLJJzo6Wu4IZUqjRo1w7do1nD17FseOHUNOTo5eFpRn/zbi30raVCqVVvF/9r6+Ks4YEwMDA2nPnD55dqI2Q0NDJCcnF5hktKxM1MaCooMpU6agYcOGqFKlCoKDg1GtWjUIIXDu3DksXLgQWVlZ+PXXX+WOKbt79+4BAN566y2ZkyhLTEwMQkNDsWbNGnh5eWHgwIH46KOPYGVlJXc0UiAhBLy8vKQPnPT0dNSrV0+6tIS+FjobG5tiFTULCwu0bt0aP/30k95cVb1r165ar03Xrl1lTPPqeIhHR3FxcRg2bBj+/fdf6Q1CpVKhTZs2+Pnnn/X2uhjJycn4+uuvsXr1ajx48AAAYGtri169emHq1KmwsbGRN6CMZs2ahfDwcNy7dw8BAQEYOHAg3n77bbljyU6j0eDixYtwcHCAEAJubm7Yu3cvPDw8tLbT1wIXERFRrO369+//mpMoy65du164TX5+Pm7fvo0FCxbA0tISmzdvLoVkVNJYUF7SgwcPcOnSJQCAp6cn7OzsZE4kn+fND7NixQq4ubnp5fwwT6jVari7u6NTp04FDg0+be7cuaWYSn5qtVrrrz3xf6eMPnufYyzoZZ09exZNmjTRm1OPGzZsiEGDBr0xe2ZZUOiVjRgxAjt27JCusvq0pKQktG3bFq1atdLb+WGKM4hYpVJh586dpZRIGYrzlzAA+Pj4vOYkynTv3j0eJn0JR48exYQJE7Bx40ZkZ2djy5YtZf5QR3EFBQVh7dq1yMvLQ/fu3REUFFSmZo59FguKDrp3716s7fTt0t4eHh5YsmQJ/P39C12/detWfPLJJ7h27VrpBiNFW758OXr27Kk1Cyj9fxqNBj4+Phg0aBB69OjB1+kp//zzj3SywqBBg1CpUiWcP38e48aNQ2RkJPz9/fX2sM7Dhw+xZs0ahIeHY8+ePahYsSICAwPRv39/lCtXTu54OmFB0cHAgQOLtV1YWNhrTqIsxsbGuHLlSpED0W7cuAFPT09kZmaWcjJSsmdPMyZtarUa/v7+2LlzJ8zNzREQEICgoCDUrVtX7miyCgkJweDBg2FnZ4cHDx7A3t4ec+fOxaeffoqePXvi888/lw4z67srV64gLCwMv/76K27duoW2bdsiKCio2H9sy65Up4WjN5Krq6vYs2dPket3794tXFxcSjGR8syfP1/07dtXmt1x+fLlonr16qJq1api/PjxIicnR+aEpe/ZmVJJ25PX5+7du2LOnDmiRo0aQq1Wi/r164uFCxeKlJQUuSPKonbt2mLWrFlCCCH++OMPoVKpRNOmTUVCQoLMyZQrPz9frF27VtjZ2ZWpWXZZUOiVDRw4ULRs2VJkZWUVWJeZmSl8fHzEwIEDZUimDN99952wtLQUPXr0EM7OzmLmzJnC3t5eTJ06VUyfPl04ODiICRMmyB2z1KlUKnHnzh25YyhWYQVu//79IjAwUFhaWgozMzPRt29fmdLJx8zMTMTFxQkhHn/wGhoair1798obSsGioqJEv379hLm5ubC2thZDhgyRO1Kx8RCPDmrXro0PP/wQAwYMgJubm9xxFOPGjRto2LAhjI2Ni5wf5siRI3r7mnl6emLWrFno3r07Tpw4gQYNGiAiIgIBAQEAgA0bNmDMmDHSWWH6Qq1Wo1atWjAweP50TGVlUqmS9rxDYBkZGVi1ahVCQ0Oxb98+GdLJ50Uz7NLj9+Tw8HCEh4fj6tWraNGiBYKCgvDBBx+UqUkhWVB0oFarYWdnh+TkZLRu3RqDBw9G165dX/gGqw+uXr2K4OBgzg9TCDMzM5w/fx7u7u4AACMjIxw7dky6rtP169dRo0YNZGRkyBmz1KnVaowaNarAVYyfNXHixFJKpCzPfhDTY2q1GlOnTpV+bsaOHYvRo0cXOOPps88+kyOerNasWYPQ0FDs2LEDjo6O6N+/PwIDA8vs+y8Lig7UajVu3LiBQ4cOITQ0FFu2bIGtrS369euHoKAgDswC54cpTKVKlbBw4UK0a9cOly5dQrVq1bBq1Sp88MEHAIDNmzcjODgYcXFxMictXfwAfr6IiAj06tWLZ+88w8PDo1in7V+9erWUEimHkZEROnbsiKCgIHTo0EGadbisYkHRwbNvqImJiQgPD0dYWBiuXLkCb29vDBo0CIGBgTInLX3Xrl3Dtm3bkJOTg5YtW6JWrVpyR1KMb7/9FkuWLEHXrl2xY8cO9OzZEytWrMD48eOhUqkwbdo0vP/++3o3URvP4iEqWXfu3IGjoyOysrKQm5sLc3NzuSO9EhYUHTzvDTU6OhohISHYsGED0tPTZUgnn6ioKHTq1AmPHj0C8PhCXaGhoejTp4/MyZQhPz8fM2fORExMDN555x2MGzcOq1evxpgxY/Dw4UN07twZP//8c5l/M9EV96A838mTJ4u1HS+bQE/cu3cPffv2xfbt25Gfn49GjRrht99+4yEefVCcN9TU1NQ3YophXTRv3hxvvfUWFi1aBBMTE3zzzTfYsGEDbt26JXc0UrDr16/D3d2dV+gtwpNLART2Fv1kub5eCiAtLQ0XL15E1apVYWFhgaNHj+LHH3/Eo0eP0K1bN2kAur4JDAzEli1b8Nlnn8HExARLliyBi4sLoqKi5I72UlhQdDBw4EDMmzcPlpaWckdRFBsbG+zfvx81atQA8HgmQysrK9y+fRv29vYypysbnuya1SdTpkwp1nYTJkx4zUmU6fr168XarkKFCq85ibLs3r0bnTp1Qnp6OmxtbbFy5Uq8//77KFeuHDQaDc6dO4fFixdj8ODBckctdW5ubli2bJk0q/elS5dQvXp1ZGRklMmxTCwoOsjIyNC73fDFUdieJZ769/+ZmZnh+vXrcHBwAAB07NgRy5Ytg4uLCwDg9u3bcHV11bu/hNVqNVxdXeHo6FjoXgLg8Z4CfT3NmArXsmVLVKlSBVOmTEFoaCjmzp2LoUOHYvr06QCAqVOn4o8//sDx48flDSoDjUaDmzdvwtnZWVpmbm6OM2fOFLhKeFnA82N18PbbbyMiIgLNmzeXO4ri/PPPP7C2tpbu5+fnY8eOHTh9+rS0rEuXLnJEk11mZqbWB/Du3bul8TpP6OPfCe3bt8fOnTvRsGFDBAYGolOnTmX+rIPXLS4uDpcvX4aLi4veDkQ/efIkfvnlF5QrVw5jx47FpEmT0LNnT2l9r1698P3338uYUF4ajabA/TL7/lJ6c8KVfaNHjxaGhobiyy+/LHTWVH2lUqleeCtL0yuXtGdnBLWwsBBXrlyR7iclJent63Pz5k0xffp04eXlJZydncWYMWPE+fPn5Y6lCEOHDhVpaWlCCCEePnwoevToIdRqtfT75OfnJ63XJ/x9KppKpRI2NjbC1tZWuqlUKmFtba21rKzgIR4dHThwAIGBgVCr1fj1119Rr149uSORwr1o5kt9PcTzrN27dyMsLAzr1q1D7dq1sX379jI162VJe/qswa+++gq//vorli9fDm9vbxw7dgz9+/fHBx98gBkzZsgdtVRpNBokJSVJh0ytrKxw4sQJVKxYEYB+/z5FREQUa7v+/fu/5iQlg4d4dNSkSRMcO3YM33zzDd555x20adOmwEyy69evlykdKZFKpdI6U+XZ+/RYo0aNcO3aNZw9exbHjh1DTk6OXheUp/92jIyMxKxZs+Dn5wcAaNasGebOnYvRo0frXUERQqBVq1bS++6TU/WNjIwAALm5uXLGk1VZKR7FxYLyErKysnDnzh2oVCpYW1tzqvsiVKpUCf/88w+qVKkidxRZCSHg5eUllZL09HTUq1dPGm+h7zsxY2JiEBoaijVr1sDLywsDBw7ERx99pHen6xfmyc9MUlJSgflO6tSpg4SEBDliyWrChAlaBb9r164FtunRo0dpRlKM/v37o1WrVvD19ZUurVGW8ZNVR9u2bUNgYCBcXFwQGxvL6e0BzJs3r9Dl8fHxCAsLk0aU6+O1MQAgLCxM7giKNGvWLISHh+PevXsICAjAnj17OOnYM7799luYmZlBrVbj1q1b0vWbAOC///7Ty7MKJ02aJHcExbp+/TqGDBmC7OxseHh4wM/PD35+fnj33XelswbLEo5B0cGQIUMQHh6Or7/+Gl9//XWB0dL6Sq1Wo1y5cgX2JF2/fh2urq4wNDTU22tjUNHUajXc3d3RqVMnafd8YfTtEgBP+Pr6au0pCAgIwKBBg6T7U6dOxfbt2xEdHS1DOvk0bNgQgwYN4l62ImRlZWH//v2Ijo5GdHQ0Dh48iJycHFSpUkUqK0+uA6Z0LCg6qFWrFgfGFuKTTz7BwYMHsWLFCq09SoaGhjhx4oQ0gZu+y8vL0yq1hw4dQn5+PurVq1cmJ1F6Vc9+ABdGpVJh586dpZSobLl69SqMjIxQvnx5uaOUqqCgIKxduxZ5eXno3r07goKC4OvrK3csxcrMzMT+/fuxZcsW/PLLL0hPTy87A4jlOn2oLEpJSRF//fWXSE1NLXJdZmamDMnkt379euHm5ibmz58vLTMwMBBnzpyRMZUyXLt2TdSvX19oNBrRrl07kZKSIlq3bi2dgl2xYkVx4cIFuWMSlRkZGRkiLCxM+Pj4CLVaLSpXriymTZsmbty4IXc0xcjKyhLR0dFi0qRJwsfHR5iYmIhKlSqJgQMHyh2t2Dgrkg7CwsLw008/FTrVvZWVFebNm4dly5bJkEx+7733HmJiYrBhwwa0b98eSUlJckdSjFGjRsHS0hJ//vknrKys0KFDB+Tm5iIhIQE3b96El5cXxo4dK3dMWaSmpmLbtm3YtGkT7t69K3ccxcnNzcXs2bNRv359WFhYwMLCAvXr18ecOXOQk5MjdzzZmJmZYcCAAYiOjsbFixfRq1cvLFmyBB4eHujYsaPenkm5e/duTJkyBX5+frCxscGQIUNw69YtfPzxx7h06RKuXLmC0NBQuWMWn9wNqSxp2LCh+Pvvv4tcHxkZKRo1alSKiZQnPz9fTJ8+XTg7OwuNRsM9KEIIBwcHcezYMSGEEMnJyUKlUok9e/ZI62NjY4WTk5NM6eRz7Ngx4eLiIu1JsrKyElu3bpU7lmI8fPhQNGvWTKjVatG2bVvx+eefi88//1y0bdtWqNVq0aJFC/Ho0SO5YypGfn6+WLt2rbCzs9PridoqVKggFi5cKJKSkuSO88p4Fo8OLl++jDp16hS5/u2338alS5dKMZHyqFQqjB8/Hm3btsXevXvL5MjxkpaZmSldBsDS0hIajUZrL5yVlRUePnwoVzzZjB07FhUrVsS6detgYmKC7777DsOHD9f736EnZs6ciYSEBBw7dqzA2U0nTpxAly5dMHPmTJ7VAiA6Olqa5M/AwEAvLxQIAGPGjEF0dDRGjBiBRYsWwcfHB76+vvDx8cFbb70ldzzdyd2QyhILCwtx5MiRItcfOXJEWFhYlGIiKguaNGkivvnmGyGEEKGhocLJyUmMGzdOWj9lyhTRoEEDueLJxt7eXsTGxkr3Hzx4IFQqlUhJSZExlXJ4eXmJP/74o8j1a9asEVWqVCnFRMqSkJAgvvvuO1G5cmWhUqlEy5YtRUREhHj48KHc0WSXlpYmNm/eLMaMGSMaN24sDA0NRc2aNcWwYcPE2rVr5Y5XbCwoOvD29hYzZ84scv306dOFt7d3KSZSjvnz54u+ffuKlStXCiGEWL58uahevbqoWrWqGD9+vMjJyZE5oXy2bt0qTExMhJGRkTAxMRG7du0SXl5eonHjxqJJkyZCo9GI1atXyx2z1D17TRUhHv8RcPXqVZkSKYuxsbGIj48vcn18fLwwNjYuxUTKsHr1auHv7y8MDAyEq6urGD9+vLh06ZLWNqdOnZIpnTL9999/4uuvvxZWVlZl6vAXD/HoIDAwECNHjkTNmjXRqVMnrXWRkZGYNm2aXs7ZMHXqVMyaNQtt27bFF198gevXr2P27Nn44osvoFar8cMPP8DQ0BCTJ0+WO6os/P39ce7cOcTGxqJBgwbw8PDA7t27sWDBAjx8+BDTp0+XpjDXN2fPntUaUC2EwLlz55CWliYt09fJ26ysrHDnzh24ubkVuj4pKanQAftvuj59+qBjx47YsGEDOnToIM3InJaWhpUrV2LZsmWIjY0tO6fSvgb5+fk4fPiwNBfKvn37kJ6eDnd3d3Tv3l3ueMXGeVB01KdPH6xYsQLVqlVD1apVAQDnz5/HxYsX8eGHH2LlypUyJyx9np6emDVrFrp3744TJ06gQYMGiIiIQEBAAABgw4YNGDNmDMcWkBa1Wg2VSlXoVP9PlqtUKr39oOnZsydyc3Oxbt26Qtf36NEDGo0Ga9asKeVk8rpz54504U3g8ZkrISEhWLduHVxdXdG9e3f06NEDjRo1kjGlPGbNmiUVkrS0NJQrVw6+vr7SjLJPLqhYVrCgvIQ1a9ZgxYoVuHTpknSdlY8++ggffvih3NFkYWZmhvPnz0vXfjAyMsKxY8ekabmvX7+OGjVqICMjQ86YssvIyEBsbCwSExOhVqtRuXJl1KtXT28vHHj9+vVibVehQoXXnESZzp49C29vb9SsWRMjR45EtWrVpD1MP/zwA86ePYsDBw5oTX+vL5KSkhAeHo6QkBCkpqbiww8/xOLFi/V+YkhXV1etQuLp6Sl3pFcj28ElemNUrFhRbNmyRQghxMWLF4VarRZr1qyR1m/atEl4eHjIFU92eXl5YvTo0cLU1FSo1WqhVqulU2srVKjw3FPXSb/FxMSIGjVqCJVKpfWzU716dbF//36548miU6dOwsrKSvTu3Vts3LhR5ObmCiE4MeSbiGNQSlBOTg4SExPfiKtI6iIgIAD9+vVD165dsWPHDowZMwZffvkl/vvvP6hUKkybNg3vv/++3DFl89VXX2Hjxo1Ys2aNdDptx44d0aVLF6xYsQIffPAB/v77b7Rt21buqKUqPj6+WNvp2+/T05o0aYIzZ87g+PHjuHjxIgDAy8sLdevWlTeYjLZs2YLPPvsMQ4cO1fsrpT9r3bp1aN++PczMzOSOUjLkbkhvkuPHj5epEdIlJS8vT0ybNk106tRJTJ8+XeTn54uVK1cKNzc3YW9vLwYMGCDS09PljikbFxcXsXv3bun+jRs3hIWFhXRZhClTpoimTZvKFU82T/YIPL1H6dll+vj7RM8XExMjBg0aJCwtLUXjxo3F/Pnzxd27d7kHRQhpwsPBgweLAwcOyB3nlXEMSgk6ceIE6tevr7eD+qhwVlZWOH78OCpVqgTg8Qh7Y2NjJCQkwNnZGWfPnkWjRo30boyOgYEBypcvjwEDBqBz584Frob9xPMmR3yTTZkypVjbTZgw4TUnUaaMjAysXr0aoaGhOHToEPLy8jB37lwEBgbq5dlNwOOB55MnT8aGDRtw/Phx1KhRA4MGDULfvn1hb28vdzydsaDooH79+s9d/+jRI1y8eFHvCkpeXh7OnDmDKlWqwNTUVGvdo0ePcOnSJdSqVUs6HVDfNGvWDB06dMDXX38NAFi1ahWGDh2KBw8eAABOnz6Nli1b4v79+3LGLHVJSUmIiIhAWFgYkpOT0adPHwQFBWldEVufPe+q6SqVChcuXEBmZqbevd8U5sKFCwgJCcGvv/6K5ORktGnTBn///bfcsUqdWq1GUlISHB0dERsbi5CQEKxcuRKPHj1Cly5dMHjwYLRp00bumMXGgqIDExMT9OrVq8hTtRITE7F06VK9e8MIDw/Hzz//jIMHD0Kj0Wity83NRZMmTTBixAj06dNHpoTy2rFjBzp27Ig6derAxMQE+/fvx+zZszFixAgAwJw5c7Blyxbs2LFD3qAy2rt3L8LCwrB27VrUqFEDQUFBCAoK0ttS+zzHjx/HuHHjsHPnTgQGBmLx4sVyR1KMvLw8REZGIjQ0VO8LyhOZmZlYu3YtQkNDsXv3bri7uyMuLk7GlDqQ8/hSWdOgQQOxcOHCItcfO3ZML4+ZN2/eXJpBtjCrV68WLVq0KMVEynP8+HHx1VdfiVGjRol///23wHrOfPlYUlKS8PPzE2q1Wvz3339yx1GUq1evioCAAGFgYCA+/PBDcfHiRbkjkcKo1eoCszM/7dKlS+Krr74qxUSvhmfx6KBZs2a4cOFCkestLS3RsmXLUkykDBcuXECTJk2KXN+oUSOcO3euFBMpT506dQqMpXgy82VISAiOHDmid3venrZ//36EhoZi7dq1qFq1KhYsWAAbGxu5YynCvXv3MHnyZPzyyy9o3rw59u/fr5eTkNGLiRccEPH09MS0adNKKc2rY0HRwU8//fTc9ZUrV8b8+fNLKY1yZGRkIDU1tcj1aWlpenm13qIUNvPlzz//LHesUpeYmIjly5cjLCwMDx48QEBAAPbt24datWrJHU0RMjIyMGfOHMydOxeenp6IjIzUu1PRSTdxcXFl86rFRWBBKQH6fg2IKlWqYP/+/UVeM2Xv3r16P19BYTNfZmVl4c8//9TbmS/d3d1Rrlw59O/fH126dIGhoSHy8/Nx8uRJre309Vo8lStXRlpaGj799FP07t0bKpWqwGsD6O/rQwVt2rQJw4YNkztGieEg2VfAa0A8NmvWLMyaNQs7d+4s8GZ54sQJtGrVCmPGjMGYMWNkSiivzp07Y/fu3ejYsSMCAgLQrl07aDQaGBoa6vXU3E8PgH0y3f+zb0f6fC2eZ1+fwt6q9fn1oYLs7OzQqFEjhIWFwdXVVe44r4x7UHTEv4QL+uKLL7BlyxY0aNAArVu3RrVq1QA8voji9u3b0axZM3zxxRcyp5QPZ74sXHHOJHj6qsb6hq8P6er06dMYPHgwatWqhXnz5pX5Mye5B0UH/Eu4aDk5Ofjhhx8KvYjiiBEjYGRkJHdE2Rw4cAAhISFYvXo1qlevjr59+6JXr15wcXHR+5+bwnDw8PPx9aEXCQ8Px8iRI+Hn54evv/66wCSIZeWwIAuKDgwMDAr9S5gFhYqDM18+Hw+ZPh9fH9LF9u3b0a5dOwghIISQDhOWpcOCnAVJB3v37kVaWhoaNGgAb29v/Pzzz7h3757csaiMMDc3R2BgIPbu3YtTp05h1KhRmDlzJhwdHdGlSxe548kiKSkJM2fORJUqVfDBBx/AyspKOmQ6c+ZMvf/w5etDL2Pu3Lno2rUr+vTpg4sXLyIuLg5Xr16V/i0zZJl9pYxLT08XISEholmzZsLQ0FCo1Wrx448/itTUVLmjyWbBggWiVatW4oMPPhDbt2/XWnf37l1RsWJFmZIpW25urtiwYYPo3Lmz3FFKXadOnYSVlZXo3bu32Lhxo8jNzRVCCF707f/w9SFdXblyRTRv3lw4OTmJP//8s9BtytKkkCwor+j8+fNi9OjRwtnZWZiYmOjlB81PP/0kzMzMRHBwsOjTp48wMjIS06dPl9YnJSXp5Qy79HwajUZ88cUXBWZE5QfwY3x9SFfm5uaiR48e4u7du1rLU1NTxZIlS0SjRo3K1HsxD/G8oqpVq2LWrFm4ceMGVq5cKXccWSxZsgRLly7Fzz//jF9//RVRUVH44Ycf9PYqq1Q8PGT6fHx9SFeLFy/GH3/8IU3Wtnv3bvTv3x8uLi6YM2cO3n33XRw4cEDmlMXHQbL0yszMzHD27Fl4eHhIy06fPo3WrVtj4MCBGDFiBFxdXcvMwCwqXRw8/Hx8fUgXhU2FsXjx4jJ5IgcLCr0yd3d3/P7772jRooXW8rNnz+Ldd9+Fv78/fvvtNxYUeqELFy4gJCQEv/76K5KTk9GmTRu9vCptUfj60PO8aVNhsKDQK/voo4/g5OSEH374ocC6M2fOwM/PD//99x8LChVbXl4eIiMjERoayg/gQvD1ocK8aVNhcAwKvbJx48YVOfFPzZo1ERUVhffee6+UU1FZptFo0K1bN374FoGvDxXmTRu3xD0o9Nro+0UUiYjk8KaMW2JBoRLHGS+JiJShLI9bYkGhEvEmjRwnInrTlMVxSywo9MretJHjREQkP4MXb0L0fFu2bCl05DgREdHL4lk89MretJHjREQkPx7ioRLzpowcJyIi+bGg0GtRlkeOExGR/FhQ6LUqiyPHiYhIfiwoREREpDgcJEtERESKw4JCREREisOCQkRERIrDgkJEijBp0iTUrVtXluceMGAAunXrJstzE1HhWFCIqEiLFy+GpaUlcnNzpWXp6ekwNDSEr6+v1rbR0dFQqVS4cuVKKad8PjmLDxG9PBYUIiqSn58f0tPTceTIEWnZnj174OzsjIMHDyIzM1NaHhUVBXd3d1SuXFmn5xBCaBWgkpKXl4f8/PwSf1wiKh0sKERUpKpVq8LFxQXR0dHSsujoaHTt2hUVK1bEgQMHtJb7+fkhKysLn332GRwdHWFiYoLmzZvj8OHDWtupVCps2bIFDRo0gLGxMfbu3Vvgua9cuYJKlSph+PDhEEIgKysLX375JcqVKwdzc3N4e3tr5QoPD4eNjQ3+/vtv1KhRA8bGxoiPjy/wuHl5eRg5ciRsbGxgb2+PMWPGgLMtECkPCwoRPZefnx+ioqKk+1FRUfD19YWPj4+0/NGjRzh48CD8/PwwZswYrFu3DhERETh69Cg8PT3h7++P+/fvaz3uuHHjMHPmTJw7dw5vv/221rqTJ0+iefPm+Oijj/Dzzz9DpVJh+PDhiImJwapVq3Dy5El88MEHaNeuHS5duiR93cOHD/H9999j2bJlOHPmDBwdHQt8P//73/8QHh6O0NBQ7N27F/fv38eGDRtK8iUjopIgiIieY+nSpcLc3Fzk5OSI1NRUYWBgIO7cuSNWrFghWrZsKYQQYseOHQKAuHbtmjA0NBS///679PXZ2dnC1dVVzJo1SwghRFRUlAAg/vzzT63nmThxoqhTp47Yt2+fsLW1FXPmzJHWXb9+XWg0GnHz5k2tr2nVqpUYP368EEKIsLAwAUAcP3680Md9wsXFRcoihBA5OTmifPnyomvXri//IhFRiTOQuR8RkcL5+voiIyMDhw8fxoMHD+Dl5QUHBwf4+Phg4MCByMzMRHR0NCpVqoSUlBTk5OSgWbNm0tcbGhqicePGOHfunNbjNmzYsMBzxcfHo02bNpg2bRpGjBghLT916hTy8vLg5eWltX1WVhbs7e2l+0ZGRgX2xjwtJSUFiYmJ8Pb2lpYZGBigYcOGPMxDpDAsKET0XJ6enihfvjyioqLw4MED+Pj4AABcXV3h5uaG/fv3IyoqCu+++65Oj2tubl5gmYODA1xdXbFy5UoEBgbCysoKwOMzhzQaDWJjY6HRaLS+xsLCQvpvU1NTqFQqXb9FIlIgjkEhohfy8/NDdHQ0oqOjtU4vbtmyJbZs2YJDhw7Bz88PlStXhpGREfbt2ydtk5OTg8OHD6NGjRovfB5TU1Ns3LgRJiYm8Pf3R1paGgCgXr16yMvLw507d+Dp6al1c3Z2Lvb3YW1tDRcXFxw8eFBalpubi9jY2GI/BhGVDhYUInohPz8/7N27F8ePH5f2oACAj48PlixZguzsbPj5+cHc3BxDhw7F6NGjsXXrVpw9exaDBw/Gw4cPERQUVKznMjc3x6ZNm2BgYID27dsjPT0dXl5eCAgIQL9+/bB+/XrExcXh0KFDmDFjBjZt2qTT9/L5559j5syZ+PPPP3H+/HkMGzYMycnJOj0GEb1+LChE9EJ+fn549OgRPD094eTkJC338fFBWlqadDoyAMycORM9evRA3759Ub9+fVy+fBn//PMPbG1ti/18FhYW2LJlC4QQ6NixIzIyMhAWFoZ+/fph1KhRqFq1Krp164bDhw/D3d1dp+9l1KhR6Nu3L/r374+mTZvC0tIS7733nk6PQUSvn0pwZBgREREpDPegEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4rCgEBERkeKwoBAREZHisKAQERGR4vw/nWBoMedLnAAAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jr9iR91ihR5R"
      },
      "source": [
        "### 5.2 A Simple Program to Read from the Web [14 points]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "axyGkceBhmPO"
      },
      "source": [
        "The cell below uses the Pandas library to read a table from the given web page (the Wikipedia information on films in the year 2010). The code loads this into a list of DataFrames called films_2010. We then pull the table at index 3, then do some simple data wrangling on top_films to set up the appropriate types.\n",
        "\n",
        "Run the cells below."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PhOV5ehZhllQ",
        "outputId": "dac347f3-4cba-43fd-aaa0-cd742dd97ba9"
      },
      "source": [
        "# CAUTION: comment this out before you submit!\n",
        "!pip install money-parser"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting money-parser\n",
            "  Downloading money_parser-0.0.1-py3-none-any.whl.metadata (5.1 kB)\n",
            "Downloading money_parser-0.0.1-py3-none-any.whl (6.4 kB)\n",
            "Installing collected packages: money-parser\n",
            "Successfully installed money-parser-0.0.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SOno1cZXoh5G"
      },
      "source": [
        "import pandas as pd\n",
        "from money_parser import price_dec"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6pYNyczHixT1"
      },
      "source": [
        "**TODO:** Read in a list of dataframes from the url https://en.wikipedia.org/wiki/2010_in_film\n",
        "\n",
        "*Hint:* Check the pandas documentation"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q_oy4SjBFxjn"
      },
      "source": [
        "def read_from_html(url):\n",
        "    import requests\n",
        "\n",
        "    headers = {\n",
        "        'User-Agent': 'Chrome/91.0.44456.123 '\n",
        "    }\n",
        "\n",
        "    try:\n",
        "        response = requests.get(url, headers=headers)\n",
        "        response.raise_for_status()\n",
        "\n",
        "        return pd.read_html(response.text)\n",
        "    except Exception as e:\n",
        "        print(f\"Error fetching data: {e}\")\n",
        "        return []"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CgrihX5biol6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7235c0b1-0ef9-4d5e-81f9-d64662a0c3fc"
      },
      "source": [
        "films_2010 = read_from_html('https://en.wikipedia.org/wiki/2010_in_film')"
      ],
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipython-input-296283384.py:12: FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.\n",
            "  return pd.read_html(response.text)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tumwfzR-jfdt"
      },
      "source": [
        "**TODO:** Find the table titled \"Highest-grossing films\"\n",
        "\n",
        "*Hint:* Click on the url, and do some digging! Check out \"Developer Tools\" for the underlying html code and check which  < table >  tag contains the desired data"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "50ZQe0mwip55"
      },
      "source": [
        "def get_film_data(df_list):\n",
        "    for i, df in enumerate(df_list):\n",
        "        if 'Rank' in df.columns and 'Title' in df.columns:\n",
        "            return df\n",
        "    return df_list[3] if len(df_list) > 3 else df_list[0]"
      ],
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RyY3UamBHvhB"
      },
      "source": [
        "top_films = get_film_data(films_2010)"
      ],
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "acY9Qu6mjqWe"
      },
      "source": [
        "**TODO:** write a method that sets the 'Rank' column as the index"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xDBT075HisUi"
      },
      "source": [
        "def set_index(df, column):\n",
        "    return df.set_index(column)"
      ],
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d6rU4qZZIRoc"
      },
      "source": [
        "top_films_ranked = set_index(top_films, 'Rank')"
      ],
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OhQfShqIkazZ"
      },
      "source": [
        "**TODO:** write a function that creates a column named 'Revenue (millions)', where the revenue in millions (rounded to 2 decimal places) are to be stored.\n",
        "\n",
        "*Hint:* We recommend you use the imported function from the 'money_parser' module (see above)."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cl72-HWiIsFw"
      },
      "source": [
        "#def extract_revenue(df, column, name):\n",
        "    #df[name] = df[column].apply(lambda x: round(price_dec(str(x))\n",
        "    #/ 1_000_000, 2) if pd.notna(x) else 0)\n",
        "    #return df\n",
        "\n",
        "\n",
        "# ValueError: Raw price value \"$828,258,695[nb 1]\" contains more than one\n",
        "#price value\n",
        "#due to this error i add cleaning of data at function"
      ],
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def extract_revenue(df, column, name):\n",
        "    def clean_and_parse(text):\n",
        "        if pd.isna(text):\n",
        "            return 0\n",
        "        import re\n",
        "        clean_text = re.sub(r'\\[.*?\\]', '', str(text))\n",
        "        clean_text = re.sub(r'[^\\d$,.]', '', clean_text)\n",
        "\n",
        "        try:\n",
        "            return price_dec(clean_text) / 1_000_000\n",
        "        except:\n",
        "            numbers = re.findall(r'[\\d,]+\\.?\\d*', clean_text)\n",
        "            if numbers:\n",
        "                return float(numbers[0].replace(',', '')) / 1_000_000\n",
        "            return 0\n",
        "\n",
        "    df[name] = df[column].apply(lambda x: round(clean_and_parse(x), 2))\n",
        "    return df"
      ],
      "metadata": {
        "id": "EAr1v0JqR4_i"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9OJyqGlYitQr"
      },
      "source": [
        "top_films_revenue = extract_revenue(top_films_ranked, 'Worldwide gross', 'Revenue (millions')"
      ],
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j8mYD0pPht0G"
      },
      "source": [
        "Can we programmatically compute how many entries were scored as top films?\n",
        "\n",
        "You can use the Python shape function on a dataframe to determine the dimensions!\n",
        "To learn more about the shape function, you can search for its pandas documentation.\n",
        "\n",
        "**TODO:** Create a function that calculates the shape of the final dataframe (top_films_revenue) and returns a tuple"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZfgUOr42h3tl"
      },
      "source": [
        "def get_dimensions(df):\n",
        "    return df.shape"
      ],
      "execution_count": 50,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "get_dimensions(top_films_revenue)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U1v9n-L6TBK6",
        "outputId": "7f83dae9-ba91-4f64-876b-f62d1ba30ee0"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10, 4)"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    }
  ]
}