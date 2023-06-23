### Sprawdzenie lab

aby sprawdzic laboratoria nalezy przeslac je do folderu lab, oraz nazwac odpowiednio lab1, lab2, etc..

Przykladowa struktura
```
lab
    -lab1
        -Jamroz_...
            -notatnik.ipynb
        -Kowalski...
            -notatnik2.jpynb
        -Grzegorz....
    -lab2
        -Jamroz_...
                    -notatnik.ipynb
                -Kowalski...
                    -notatnik2.jpynb
                -Grzegorz....
```

<u>WAZNE ABY BYL TAM MAKSYMALNIE JEDEN PLIK</u>

### Rezultat
```
Rezultat mozna obserwowac w excelu Result.xslx, w ktorym
bedzie podana informacja o tym jak wyglada sytuacja z przeslanymi /
nieprzeslanymi zadaniami oraz odpowiednie sprawdzenie poprawnosci 
wykonanych zadan.
```

### exercises.json
Przykladowy plik exercises.json mozna znalezc ponizej. Okresla on numer laboratorium, zadania oraz serie danych </br>
na ktorych mozemy testowac <br>

struktura wyglada nastepujaca, przy czym istotnym czynnikiem tutaj jest
data_series oraz expected_outputs. Data_series jest to 
tablica, tablic obiektow, ktore odpowiadaja za zamockowanie danych 
w naszej aplikacji. Innymi slowy jezeli w zadaniu wystapi
a = int(input("cokolwike")) to nasza aplikacja pojdzie do data series 
i zobaczy ze chce type: int zamienic na content: 3. czyli a = 3
</br>

<b>WZOR</b></br>
<u>zmienna = <b>type</b>(input("....."))</u></br>
<u>zmienna = <b>3</b></u>
</br>
## UWAGA 
ponizej przesylam przygotowany plik exercises.json (Aktualnie umieszczony jest pusty, jako ze aktualne zadania 
wyslane przez studentow nie sa przygotowane na sprawdzenie)
```
{
  "lab_1": {
    "zadanie 1": {
      "expected_outputs": [
        "pole 473.7410112522892\nobjetosc 710.6115168784338"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "float",
            "content": 3
          },
          {
            "type": "float",
            "content": 4
          }
        ]
      ]
    },
    "zadanie 2": {
      "expected_outputs": [
        "Liczba: 2.3"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "float",
            "content": 2.23
          },
          {
            "type": "int",
            "content": 1
          }
        ]
      ]
    },
    "zadanie 3": {
      "expected_outputs": [
        "Formaty przekształcenia dla liczb całkowitych:\ni |1|\ni |         1|\ni |        +1|\ni |1         |\ni |0000000001|\ni |     00001|\n\nFormaty przekształcenia dla liczb rzeczywistych:\nx |2.5|\nx |       2.5|\nx |   +2.5000|\nx |2.5000    |\nx |00002.5000|\nx |2.5000e+00|"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "int",
            "content": 1
          },
          {
            "type": "float",
            "content": 2.5
          }
        ]
      ]
    },
    "zadanie 4": {
      "expected_outputs": [
        "xdxmxxs"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "str",
            "content": "'adamuos'"
          },
          {
            "type": "str",
            "content": "'x'"
          }
        ]
      ]
    },
    "zadanie 5": {
      "expected_outputs": [
        "Tekst: bba liczba: 1"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "str",
            "content": "'aa'"
          },
          {
            "type": "str",
            "content": "'bb'"
          },
          {
            "type": "int",
            "content": 1
          }
        ]
      ]
    },
    "zadanie 6": {
      "expected_outputs": [
        "suma = 46 iloczyn = 1"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "int",
            "content": 10
          },
          {
            "type": "int",
            "content": 12
          },
          {
            "type": "int",
            "content": 13
          }
        ]
      ]
    },
    "zadanie 7": {
      "expected_outputs": [
        "Taki dzien nie istnieje\nNie znasz dni tygodnia"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "str",
            "content": "'cos'"
          },
          {
            "type": "str",
            "content": "'2'"
          }
        ]
      ]
    },
    "zadanie 8": {
      "expected_outputs": [
        "7 jest liczbą pierwszą."
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": [
        [
          {
            "type": "int",
            "content": 7
          }
        ]
      ]
    }
  },
  "lab_2": {
    "zadanie 1": {
      "expected_outputs": [
        "Liczba Mersenne'a: 1\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 3\nCzy jest liczbą pierwszą: None\nLiczba Mersenne'a: 7\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 15\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 31\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 63\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 127\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 255\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 511\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 1023\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 2047\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 4095\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 8191\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 16383\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 32767\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 65535\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 131071\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 262143\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 524287\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 1048575\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 2097151\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 4194303\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 8388607\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 16777215\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 33554431\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 67108863\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 134217727\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 268435455\nCzy jest liczbą pierwszą: False\nLiczba Mersenne'a: 536870911\nCzy jest liczbą pierwszą: True\nLiczba Mersenne'a: 1073741823\nCzy jest liczbą pierwszą: False"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 3": {
      "expected_outputs": [
        "-1.0 5.0\n-0.7777777777777778 5.222222222222222\n-0.5555555555555556 5.444444444444445\n-0.33333333333333337 5.666666666666667\n-0.11111111111111116 5.888888888888889\n0.11111111111111116 6.111111111111111\n0.33333333333333326 6.333333333333333\n0.5555555555555554 6.555555555555555\n0.7777777777777777 6.777777777777778\n1.0 7.0"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    }
  },
  "lab_3": {
    "zadanie 1": {
      "expected_outputs": [
        "[0, 0, 8, 0, 8, 0]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 2": {
      "expected_outputs": [
        "True"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 3": {
      "expected_outputs": [
        "[1, 8, 3.5]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 4": {
      "expected_outputs": [
        "[1, 3, 8, 2, 2, 5]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 5": {
      "expected_outputs": [
        "[1, 4.5, 2.5, 5.0, 3.5, 5]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 6": {
      "expected_outputs": [
        "['KS', 'au', 'ml', 'iż', 'ly']"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 7": {
      "expected_outputs": [
        "[0.9036144578313253, 0.8290598290598291, 1.0092592592592593, 0.27631578947368424, 0.8925619834710744]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 8": {
      "expected_outputs": [
        "[2, 2, 1, 8, 5]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 9": {
      "expected_outputs": [
        "[]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 10": {
      "expected_outputs": [
        "[1, 3, 0, 8, 2, 0, 2, 5]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 11": {
      "expected_outputs": [
        "[1, 0, 1, 0, 1, 0, 1, 0]\n[0, 1, 0, 1, 0, 1, 0, 1]\n[1, 0, 1, 0, 1, 0, 1, 0]\n[0, 1, 0, 1, 0, 1, 0, 1]\n[1, 0, 1, 0, 1, 0, 1, 0]\n[0, 1, 0, 1, 0, 1, 0, 1]\n[1, 0, 1, 0, 1, 0, 1, 0]\n[0, 1, 0, 1, 0, 1, 0, 1]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 12": {
      "expected_outputs": [
        "['przykładowy', 'zadania', 'dwunastego']"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 13": {
      "expected_outputs": [
        "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 30]"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    }
  },
  "lab_6": {
    "zadanie 1": {
      "expected_outputs": [
        "Upss\nl\nUpss\n \nm\nUpss\n \nk\nUpss\nt\nUpss"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 2": {
      "expected_outputs": [
        "1\n2\n3\n4\n5\n6\n7"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 3": {
      "expected_outputs": [
        "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37\n41\n43\n47\n53\n59\n61\n67\n71\n73\n79\n83\n89\n97"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 5": {
      "expected_outputs": [
        "Dodano monetę 0.01 PLN\nDodano monetę 0.05 PLN\nDodano monetę 0.02 PLN\nWszystkie monety:\n(Decimal('0.01'), 'PLN')\n(Decimal('0.02'), 'PLN')\n(Decimal('0.05'), 'PLN')"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 6": {
      "expected_outputs": [
        "70"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 7": {
      "expected_outputs": [
        "Otrzymano: 1\nGenerator zwrócił: 1\nOtrzymano: 2\nGenerator zwrócił: 3\nOtrzymano: 3\nGenerator zwrócił: 6\nOtrzymano: 5\nGenerator zwrócił: 11\nOtrzymano: 7\nGenerator zwrócił: 18\nOtrzymano: 11\nGenerator zwrócił: 29"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 8": {
      "expected_outputs": [
        "0\n1"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    },
    "zadanie 9": {
      "expected_outputs": [
        "1337\n0\n1\n1337"
      ],
      "plagiarism_quantity": 0.85,
      "process_input": false,
      "data_series": []
    }
  }
}
```