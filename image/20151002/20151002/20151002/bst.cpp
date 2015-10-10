#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//	노드 자료구조
struct bst
{
	int key;			//	노드에 저장되는 키값.
	bst *left, *right;	//	왼쪽, 오른쪽 서브트리
};
//	for C.
typedef struct _bst
{
	int key;			//	노드에 저장되는 키값.
	struct _bst *left, *right;	//	왼쪽, 오른쪽 서브트리
} BST;

//	root로 시작하는 이진검색트리에서,
//	지정한 key 값이 있는 경우 해당 노드 포인터 반환.
//	없으면 NULL 반환.
bst *bstSearch(bst *root, int key)
{
#if 0
	//	트리가 비어있다면 NULL 반환.
	if( root == NULL ) return NULL;
	if( root->key == key ) return root;
	if( key < root->key ) 
		return bstSearch(root->left, key);
	else return bstSearch(root->right, key);
#else
	while( root )
	{
		if( root->key == key ) return root;
		if( key < root->key ) root = root->left;
		else root = root->right;
	}
	return NULL;
#endif
}

//	root로 시작하는 이진검색트리에서,
//	지정한 key 값의 노드를 삽입한다.
void bstInsert(bst **root, int key)
{
#if 0
	//	트리가 비어있는 경우 새로운 데이터를
	//	삽입한다.
	if( *root == NULL )
	{
		*root = new bst();
		(*root)->key = key;
		(*root)->left = (*root)->right = NULL;
		return;
	}
	//	현재 트리의 root key값이 같은 경우 무시.
	if( (*root)->key == key ) return;
	if( key < (*root)->key )
		bstInsert(&(*root)->left, key);
	else bstInsert(&(*root)->right, key);
#else
	while( *root )
	{
		if( (*root)->key == key ) return;
		if( key < (*root)->key ) root = &(*root)->left;
		else root = &(*root)->right;
	}
	*root = new bst();
	(*root)->key = key;
	(*root)->left = (*root)->right = NULL;
#endif
}

//	root 트리에서 key값을 가지는 노드를 삭제한다.
void bstRemove(bst **root, int key)
{
	//	1. key값을 가지는 노드를 찾는다.
	while( *root )
	{
		if( (*root)->key == key ) break;
		if( key < (*root)->key ) root = &(*root)->left;
		else root = &(*root)->right;
	}
	if( *root == NULL ) return;
	
	//	2-1. 자식이 하나도 없는 경우.
	if( (*root)->left == NULL && (*root)->right == NULL )
	{
		bst *p = *root;
		*root = NULL;
		delete p;
	}
	//	2-2-1. 왼쪽 자식만 있는 경우.
	else if( (*root)->right == NULL )
	{
		bst *p = *root;
		*root = p->left;
		delete p;
	}
	//	2-2-2. 오른쪽 자식만 있는 경우.
	else if( (*root)->left == NULL )
	{
		bst *p = *root;
		*root = p->right;
		delete p;
	}
	//	2-3. 자식이 둘인 경우.
	else
	{
		//	1) 현재 노드의 오른쪽 서브트리의 제일 왼쪽 노드를 찾는다.
		//	오른쪽 서브트리의 제일 왼쪽 노드는 현재 노드 key 값보다
		//	큰 노드 중 제일 작은 값이다.
		bst **s = &(*root)->right;
		while( (*s)->left ) s = &(*s)->left;
		//	2) 제일왼쪽 노드의 값을 현재 노드에 복사한다.
		bst *r = *s;
		(*root)->key = r->key;
		//	3) 제일왼쪽 노드는 자식이 하나이므로 CASE 2로 처리 삭제한다.
		*s = r->right;
		delete r;
	}
}

//	root 트리의 값들을 출력한다.
void bstDisplay(bst *root)
{
	if( root == NULL ) return;
	bstDisplay(root->left);
	printf("[%d]", root->key);
	bstDisplay(root->right);
}

int main()
{
	bst *root = NULL;			//	전체 BST의 root노드

	while(1)
	{
		int cmd, key;
		printf("1. Insert/2. Search/3. Remove/"
			"4. Display/0. Quit/Command = ");
		scanf("%d", &cmd);
		if( cmd == 0 ) break;
		if( cmd == 1 )
		{
			printf("Enter key value for Insertion : ");
			scanf("%d", &key);
			bstInsert(&root, key);
		}
		else if( cmd == 2 )
		{
			printf("Enter key value for searching : ");
			scanf("%d", &key);
			bst *res = bstSearch(root, key);
			if( res == NULL ) printf("Not found\n");
			else printf("Found : %d\n", res->key);
		}
		else if( cmd == 3 )
		{
			printf("Enter key value for removing : ");
			scanf("%d", &key);
			bstRemove(&root, key);
		}
		else if( cmd == 4 )
		{
			bstDisplay(root);
			putchar('\n');
		}
	}
	return 0;
}










