// C++ Code
#include <algorithm>
#include <bits/stdc++.h>
#include <map>
#include <vector>

using namespace std;

// Input matrix
vector<vector<int> > arr
    = { { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
        { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
        { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
        { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
        { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
        { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
        { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
        { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
        { 0, 0, 5, 2, 0, 6, 3, 0, 0 } };

// Position of the input elements in the arr
// pos = {
//     element: [[position 1], [position 2]]
// }
map<int, vector<vector<int> > > pos;

// Count of the remaining number of the elements
// rem = {
//     element: pending count
// }
map<int, int> rem;

// Graph defining tentative positions of the elements to be
// filled graph = {
//     key: {
//         row1: [columns],
//         row2: [columns]
//     }
// }
map<int, map<int, vector<int> > > graph;

// Print the matrix array
void printMatrix()
{
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cout << arr[i][j] << " ";
    }
    cout << endl;
  }
}

// Method to check if the inserted element is safe
bool is_safe(int x, int y)
{
  int key = arr[x][y];
  for (int i = 0; i < 9; i++) {
    if (i != y && arr[x][i] == key) {
      return false;
    }
    if (i != x && arr[i][y] == key) {
      return false;
    }
  }

  int r_start = floor(x / 3) * 3;
  int r_end = r_start + 3;

  int c_start = floor(y / 3) * 3;
  int c_end = c_start + 3;

  for (int i = r_start; i < r_end; i++) {
    for (int j = c_start; j < c_end; j++) {
      if (i != x && j != y && arr[i][j] == key) {
        return false;
      }
    }
  }
  return true;
}

// method to fill the matrix
// input keys: list of elements to be filled in the matrix
//        k   : index number of the element to be picked up
//        from keys rows: list of row index where element is
//        to be inserted r   : index number of the row to be
//        inserted
//
bool fill_matrix(int k, vector<int> keys, int r,
                 vector<int> rows)
{
  int c = 0;
  arr[rows[r]][c] = keys[k];
  if (is_safe(rows[r], c)) {
    if (r < rows.size() - 1) {
      if (fill_matrix(k, keys, r + 1, rows)) {
        return true;
      }
      else {
        arr[rows[r]][c] = 0;
      }
    }
    else {
      if (k < keys.size() - 1) {
        if (fill_matrix(
          k + 1, keys, 0,
          rows)) {
          return true;
        }
        else {
          arr[rows[r]][c] = 0;

        }
      }
      return true;
    }
  }
  arr[rows[r]][c] = 0;

  return false;
}

// Fill the pos and rem dictionary. It will be used to build
// graph
void build_pos_and_rem()
{
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      if (arr[i][j] > 0) {
        if (!pos.count(arr[i][j])) {
          pos[arr[i][j]] = {};
        }
        pos[arr[i][j]].push_back({ i, j });
        if (!rem.count(arr[i][j])) {
          rem[arr[i][j]] = 9;
        }
        rem[arr[i][j]] -= 1;
      }
    }
  }

  // Fill the elements not present in input matrix.
  // Example: 1 is missing in input matrix
  for (int i = 1; i < 10; i++) {
    if (!pos.count(i)) {
      pos[i] = {};
    }
    if (!rem.count(i)) {
      rem[i] = 9;
    }
  }
}

int main() 
{ 
    printMatrix(); 
}