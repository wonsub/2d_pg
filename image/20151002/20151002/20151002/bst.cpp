#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//	��� �ڷᱸ��
struct bst
{
	int key;			//	��忡 ����Ǵ� Ű��.
	bst *left, *right;	//	����, ������ ����Ʈ��
};
//	for C.
typedef struct _bst
{
	int key;			//	��忡 ����Ǵ� Ű��.
	struct _bst *left, *right;	//	����, ������ ����Ʈ��
} BST;

//	root�� �����ϴ� �����˻�Ʈ������,
//	������ key ���� �ִ� ��� �ش� ��� ������ ��ȯ.
//	������ NULL ��ȯ.
bst *bstSearch(bst *root, int key)
{
#if 0
	//	Ʈ���� ����ִٸ� NULL ��ȯ.
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

//	root�� �����ϴ� �����˻�Ʈ������,
//	������ key ���� ��带 �����Ѵ�.
void bstInsert(bst **root, int key)
{
#if 0
	//	Ʈ���� ����ִ� ��� ���ο� �����͸�
	//	�����Ѵ�.
	if( *root == NULL )
	{
		*root = new bst();
		(*root)->key = key;
		(*root)->left = (*root)->right = NULL;
		return;
	}
	//	���� Ʈ���� root key���� ���� ��� ����.
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

//	root Ʈ������ key���� ������ ��带 �����Ѵ�.
void bstRemove(bst **root, int key)
{
	//	1. key���� ������ ��带 ã�´�.
	while( *root )
	{
		if( (*root)->key == key ) break;
		if( key < (*root)->key ) root = &(*root)->left;
		else root = &(*root)->right;
	}
	if( *root == NULL ) return;
	
	//	2-1. �ڽ��� �ϳ��� ���� ���.
	if( (*root)->left == NULL && (*root)->right == NULL )
	{
		bst *p = *root;
		*root = NULL;
		delete p;
	}
	//	2-2-1. ���� �ڽĸ� �ִ� ���.
	else if( (*root)->right == NULL )
	{
		bst *p = *root;
		*root = p->left;
		delete p;
	}
	//	2-2-2. ������ �ڽĸ� �ִ� ���.
	else if( (*root)->left == NULL )
	{
		bst *p = *root;
		*root = p->right;
		delete p;
	}
	//	2-3. �ڽ��� ���� ���.
	else
	{
		//	1) ���� ����� ������ ����Ʈ���� ���� ���� ��带 ã�´�.
		//	������ ����Ʈ���� ���� ���� ���� ���� ��� key ������
		//	ū ��� �� ���� ���� ���̴�.
		bst **s = &(*root)->right;
		while( (*s)->left ) s = &(*s)->left;
		//	2) ���Ͽ��� ����� ���� ���� ��忡 �����Ѵ�.
		bst *r = *s;
		(*root)->key = r->key;
		//	3) ���Ͽ��� ���� �ڽ��� �ϳ��̹Ƿ� CASE 2�� ó�� �����Ѵ�.
		*s = r->right;
		delete r;
	}
}

//	root Ʈ���� ������ ����Ѵ�.
void bstDisplay(bst *root)
{
	if( root == NULL ) return;
	bstDisplay(root->left);
	printf("[%d]", root->key);
	bstDisplay(root->right);
}

int main()
{
	bst *root = NULL;			//	��ü BST�� root���

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










