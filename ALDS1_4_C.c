#include <stdio.h>
#include <string.h>

#define M 1200007 /* prime number */
#define L 14

char H[M][L]; /* Hash Table */

int char_id_for(char ch) {
  if ('A' == ch) return 1;
  if ('C' == ch) return 2;
  if ('G' == ch) return 3;
  if ('T' == ch) return 4;
  return -1;
}

typedef long long hash_key;
/* convert a string into an integer value */
hash_key key_for(char str[]) {
  long long sum = 0, p = 1;
  int len = strlen(str);
  for (int i = 0; i < len; i++) {
    sum += p*(char_id_for(str[i]));
    p *= 5;
  }
  return sum;
}

int h(hash_key k) {
    return k % M;
}

int g(hash_key k) {
    return 14 - k%13;
}

#define NOT_FOUND -1
int find(char str[]) {
    hash_key k = key_for(str);
    int n = h(k);
    int m = g(k);
    for (int c = 0; c < M; c++) {
        if ('\0' == H[n][0]) break;
        if (0 == strcmp(H[n], str)) {
            return n;
        }
        n = (n + m) % M;
    }
    return NOT_FOUND;
}

#define INSERT_OK 1
#define INSERT_ERROR -1
int insert(char str[]) {
    int n, m;
    hash_key k;

    if (0 <= find(str)) return INSERT_OK;

    k = key_for(str);
    n = h(k);
    m = g(k);
    for (int c = 0; c < M; c++) {
        if ('\0' == H[n][0]) {
            strcpy(H[n], str);
            return n;
        }
        n = (n + m) % M;
    }
    return INSERT_ERROR;
}

void init_hash_table() {
    for (int i = 0; i < M; i++) {
        H[i][0] = '\0';
    }
}

int main(){
    int n;
    char str[L], cmd[9];

    init_hash_table();
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%s %s\n", cmd, str);
        
        if ('i' == cmd[0]){
            insert(str);
            continue;
        }
        puts(0 <= find(str) ? "yes" : "no");
    }
    return 0;
}
