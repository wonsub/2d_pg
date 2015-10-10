#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>

class Bst
{
public:
	struct bst
	{
		bst() : left(NULL), right(NULL) { }
		int key;
		bst *left, *right;
	};

	Bst() : root(NULL) { }
	bst *Search(int key)
	{
		bst *p = root;
		while( p )
		{
			if( p->key == key ) return p;
			if( key < p->key ) p = p->left;
			else p = p->right;
		}
		return NULL;
	}
	void Insert(int key)
	{
#if 0
		bst **p = &root;
		while( *p )
		{
			if( (*p)->key == key ) return;
			if( key < (*p)->key ) p = &(*p)->left;
			else p = &(*p)->right;
		}
		*p = new bst;
		(*p)->key = key;
#else
		bst *p = NULL, *c = root;
		while( c )
		{
			if( key == c->key ) return;
			p = c;
			if( key < c->key ) c = c->left;
			else c = c->right;
		}
		c = new bst(); c->key = key;
		if( p == NULL ) root = c;
		else if( key < p->key ) p->left = c;
		else p->right = c;
#endif
	}
	void Remove(int key)
	{
		bst **p = &root;
		while(*p)
		{
			if( (*p)->key == key ) break;
			if( key < (*p)->key ) p = &(*p)->left;
			else p = &(*p)->right;
		}
		if( *p == NULL ) return;
		if( (*p)->left == NULL && (*p)->right == NULL )
		{
			bst *r = *p;
			*p = NULL;
			delete r;
		}
		else if( (*p)->right == NULL )
		{
			bst *r = *p;
			*p = r->left;
			delete r;
		}
		else if( (*p)->left == NULL )
		{
			bst *r = *p;
			*p = r->right;
			delete r;
		}
		else
		{
			bst **s = &(*p)->right;
			while( (*s)->left ) s = &(*s)->left;
			bst *r = *s;
			(*p)->key = r->key;
			*s = r->right;
			delete r;
		}
	}
	void Display(bst *p) const
	{
		if( p == NULL ) return;
		Display(p->left);
		printf("[%d]", p->key);
		Display(p->right);
	}
	void Display() const { Display(root); putchar('\n'); }

private:
	bst *root;
};

int main()
{
	Bst bst;
	for( ; ; )
	{
		printf("1. Insert/2. Search/3. Remove/4.Display/0. Quit/Command : ");
		int cmd, key;
		scanf("%d", &cmd);
		if( cmd == 0 ) break;
		if( cmd == 1 )
		{
			printf("Enter value for Inserting : ");
			scanf("%d", &key);
			bst.Insert(key);
		}
		else if( cmd == 2 )
		{
			printf("Enter value for serching  : ");
			scanf("%d", &key);
			Bst::bst *res = bst.Search(key);
			if( res == NULL ) printf("Not found\n");
			else printf("found %d\n", res->key);
		}
		else if( cmd == 3 )
		{
			printf("Enter value for Removing : ");
			scanf("%d", &key);
			bst.Remove(key);
		}
		else if( cmd == 4 ) { bst.Display(); }
	}
	
	return 0;
}





