#include <stdio.h>
#include <stdint.h>

#define bd_place(bd,r,c) ( (bd) |= ((uint64_t)1 << ((8*(r))+(c))) )
#define bd_test(bd,r,c)  ( (bd) & ((uint64_t)1 << ((8*(r))+(c))) )

#define use_r(u,r) ( (u) |= ((uint64_t)1<<(r)) )
#define use_c(u,c) ( (u) |= ((uint64_t)1<<(8+(c))) )
#define use_up(u,x) ( (u) |= ((uint64_t)1<<(16+(x))) )
#define use_down(u,y) ( (u) |= ((uint64_t)1<<(32+(y))) )
#define use_at(u,r,c) \
    do { \
        use_r((u),(r)); \
        use_c((u),(c)); \
        use_up((u),((r)+(c))); \
        use_down((u),((r)-(c)+7)); \
    } while(0)

#define used_r(u,r) ( (u) & ((uint64_t)1<<(r)) )
#define used_c(u,c) ( (u) & ((uint64_t)1<<(8+(c))) )
#define used_up(u,x) ( (u) & ((uint64_t)1<<(16+(x))) )
#define used_down(u,y) ( (u) & ((uint64_t)1<<(32+(y))) )
#define used_updown(u,r,c) ( \
    used_up((u),((r)+(c))) \
    || used_down((u),((r)-(c)+7)) \
)

int
load_Qs(uint64_t *board, uint64_t *used)
{
    int r, c;
    while (EOF != scanf("%d %d\n", &r, &c)) {
        bd_place(*board, r, c);
        use_at(*used, r, c);
    }
    return 0;
}

int
search_ans(int r, uint64_t *board, uint64_t *used)
{
    uint64_t tmp_bd = *board;
    uint64_t tmp_used = *used;

    if (8 == r) return 0;
    if (used_r(*used, r)) {
        return search_ans(r+1, board, used);
    }
    
    for (int c = 0; c < 8; c++) {
        if (used_c(*used, c) || used_updown(*used, r, c)) continue;

        bd_place(*board, r, c);
        use_at(*used, r, c);
        if (!search_ans(r+1, board, used)) return 0;
        *board = tmp_bd;
        *used = tmp_used;
    }
    return -1;
}

void
print_ans(uint64_t *board)
{
    for (int r = 0; r < 8; r++) {
        for (int c = 0; c < 8; c++) {
            putchar(bd_test(*board, r, c) ? 'Q' : '.' );
        }
        puts("");
    }
}

int
main(int argc, char *argv[])
{
    int n;
    uint64_t board = 0;
    uint64_t used  = 0;

    if (1 != scanf("%d\n", &n)) return -1;
    if ((n <= 0) || (8 < n)) return -1;

    if (load_Qs(&board, &used)) return -1;
    if (search_ans(0, &board, &used)) return -1;

    print_ans(&board);
    return 0;
}
