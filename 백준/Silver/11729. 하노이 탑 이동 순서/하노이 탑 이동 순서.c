#include<stdio.h>
#pragma warning(disable:4996)


/* 일단 하노이 탑의 문제의 핵심은
A에서의 맨 밑에 있는 원반이 C로 이동하는 걸 첫 번째로 생각함
따라서 A에서 위에 있는 n-1개의 원반들을 B로 옮겨야함
그리고 A의 맨 밑에 있는 큰 원반을 C로 옮기고
B에 있는 n-1개의 원반들을 C로 옮기는 작업을 함*/

void hanoi_move(int num, char from, char by, char to);  // 옮긴 상황을 알려주는 함수
void hanoi_count(int num, char from, char by, char to); //옮긴 횟수를 계산하는 함수

int count = 0;

int main(void)
{
	int n;
	scanf("%d", &n);
	hanoi_count(n, '1', '2', '3');
	printf("%d\n", count);
	hanoi_move(n, '1', '2', '3');

}

void hanoi_count(int num, char from, char by, char to)
{
	if (num == 1)
	{
		count++;
		return;
	}

	hanoi_count(num - 1, from, to, by);
	count++;
	hanoi_count(num - 1, by, from, to);
}

void hanoi_move(int num, char from, char by, char to)
{
	count++;
	if (num == 1)
	{
		printf("%c %c\n", from, to);
		return;
	}

	hanoi_move(num - 1, from, to, by); // n-1개를 일단 B로 보내는 작업
	printf("%c %c\n", from, to); // 마지막 큰 원반을 C로 보내는 작업
	hanoi_move(num - 1, by, from, to); //B에 있던 n-1개를 C로 보내는 작업
}