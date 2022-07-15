//#include <bits/stdc++.h> not standard c++ :(
#include <iostream>

#include <string>

#include <cmath>

using namespace std;

void move_arr(char arr[7][7], char c, int state) {
  for (int i = 0; i < 7; i++) {
    for (int j = 0; j < 7; j++) {

      //find the value int the array that equals to the character given
      if (c == arr[i][j]) {

        //if the value given is on the two diagonal lines
        if (i == j || i + j == 6) {
          if (state == 1) {

            // rotate the array by removing the frist value and move every value once, then adding the value at the back of the array
            char temp_value_holder = arr[6][j];
            int k;
            for (k = 6; k > 0; k--)
              arr[k][j] = arr[k - 1][j];
            arr[k][j] = temp_value_holder;
            //  cout << "a";
            return;
          }
          if (state == 2) {

            // rotate the array by removing the frist value and move every value once, then adding the value at the back of the array
            char temp_value_holder = arr[i][6];
            int k;
            for (k = 6; k > 0; k--)
              arr[i][k] = arr[i][k - 1];
            arr[i][k] = temp_value_holder;
            // cout << "a";
            return;
          }

        } else {
          if (state == 1) {

            // rotate the array by removing the frist value and move every value once, then adding the value at the back of the array
            char temp_value_holder = arr[i][6];
            int k;
            for (k = 6; k > 0; k--)
              arr[i][k] = arr[i][k - 1];
            arr[i][k] = temp_value_holder;
            //cout << "a";
            return;
          }
          if (state == 2) {

            // rotate the array by removing the frist value and move every value once, then adding the value at the back of the array
            char temp_value_holder = arr[6][j];
            int k;
            for (k = 6; k > 0; k--)
              arr[k][j] = arr[k - 1][j];
            arr[k][j] = temp_value_holder;
            //  cout << "a";
            return;
          }
        }
      }
    }
  }
}

char encryfull_plain_text_letter(char arr[7][7], char k, char c) {
  // find the value of the key and the character in the array
  int kx, ky, cx, cy;
  for (int i = 0; i < 7; i++) {
    for (int j = 0; j < 7; j++) {
      if (arr[i][j] == k) {
        kx = i;
        ky = j;
      }
    }
  }
  for (int i = 0; i < 7; i++) {
    for (int j = 0; j < 7; j++) {
      if (arr[i][j] == c) {
        cx = i;
        cy = j;
      }
    }
  }

  //find the distance between the two values
  int dx = kx - cx;
  int dy = ky - cy;

  //find the new value by adding the distance to the key
  int nx = (kx + dx);
  int ny = (ky + dy);

  //if value is greater than 6 and smaller than 0 minus 7 from it or plus 7 to it.
  if (nx <= -1) {
    nx += 7;
  } else if (nx >= 7) {
    nx -= 7;
  }

  if (ny <= -1) {
    ny += 7;
  } else if (ny >= 7) {
    ny -= 7;
  }
  //  cout << nx << endl << ny;

  //return the encrypted character
  return arr[nx][ny];
}

int main() {
  //get input file and state the output value
  //std::ifstream cin("ecin.txt");
 // std::ofstream cout("ecout.txt");

  //create and enter key and key length
  string up_key;
  cout << "Enter Key1: ";
  getline(cin, up_key);
  string key;

  // turn the entered key into lowercase
  for (int i = 0; i < up_key.length(); i++) {
    key += tolower(up_key[i]);
  }
  int key_length = up_key.length();

  //creat the 7x7 matrix
  char arr[7][7] = {
    {
      'a',
      'b',
      'c',
      'd',
      'e',
      'f',
      'g'
    },
    {
      'h',
      'i',
      'j',
      'k',
      'l',
      'm',
      'n'
    },
    {
      'o',
      'p',
      'q',
      'r',
      's',
      't',
      'u'
    },
    {
      'v',
      'w',
      'x',
      'y',
      'z',
      '!',
      '@'
    },
    {
      '#',
      '$',
      '%',
      ' ',
      '&',
      '*',
      '('
    },
    {
      ')',
      ',',
      '.',
      ';',
      '/',
      '\'',
      '\\'
    },
    {
      '\"',
      '[',
      ']',
      '{',
      '}',
      ':',
      '-'
    }
  };

  //for each letter in the key, move_arr the array with the key and the state of is it odd or even
  for (int i = 0; i < key_length; i++) {
    if ((i + 1) % 2 == 0) move_arr(arr, key[i], 2);
    else move_arr(arr, key[i], 1);
  }
    
    //the second key that is one character
    char key2;
    cout << "Enter Key2: ";
    cin >> key2;
    
  //enter plain text, if we use getline, it will get a \n from before, but if we use cin to get the first character, it will ignore the \n and get the first character
  cout << "Enter Plain Text: ";
  char first_character;
  cin >> first_character;
  string plain_text_before;
  getline(cin, plain_text_before);

  

  //combine add the first character and ther plain text
  string up_full_plain_text = first_character + plain_text_before;
  string full_plain_text;

  //turn all the uppercase character to lowercase
  for (int i = 0; i < up_full_plain_text.length(); i++) {
    full_plain_text += tolower(up_full_plain_text[i]);
  }

  //cout << full_plain_text << endl;
  int plain_text_length = full_plain_text.length();

  // for each character, encrypt and add to new string
    cout << "Enter E or D: ";
    char type;
    cin >> type;
    if(type == 'e'){
 string encrypted_str = "";
  for (int i = 0; i < plain_text_length; i++) {
    if (i == 0)
      encrypted_str += encryfull_plain_text_letter(arr, key2, full_plain_text[i]);
    else
      encrypted_str += encryfull_plain_text_letter(arr, full_plain_text[i - 1], full_plain_text[i]);
  }
  cout << "Encrypted Text: " << encrypted_str << endl;
}

if(type == 'd'){
  string decrypted_str = "";
  for (int i = 0; i < plain_text_length; i++) {
    if (i == 0)
      decrypted_str += encryfull_plain_text_letter(arr, key2, full_plain_text[i]);
    else
      decrypted_str += encryfull_plain_text_letter(arr, decrypted_str[i - 1], full_plain_text[i]);
  }
  cout << "Decrypted Text: " << decrypted_str << endl;
}

}
