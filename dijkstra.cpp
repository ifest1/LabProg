#include <iostream>

struct node
{
    int vertex;
    int distance;
    struct node *next;
};

struct queue
{
    struct node *first, *last;
};

struct node *new_node(int vertex, int distance)
{
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->vertex = vertex;
    node->distance = distance;
    node->next = NULL;
    return node;
}

struct queue *create_queue()
{
    struct queue *q = (struct queue *)malloc(sizeof(struct queue));
    q->first = q->last = NULL;
    return q;
}

void enqueue(struct queue *q, int vertex, int distance)
{
    struct node *temp = new_node(vertex, distance);

    if (q->last == NULL)
    {
        q->first = q->last = temp;
        return;
    }
    q->last->next = temp;
    q->last = temp;
}

struct node *dequeue(struct queue *q)
{
    int data;
    if (q->last == NULL)
        return NULL;
    else
    {
        struct node *temp = q->first;
        q->first = q->first->next;

        if (q->first == NULL)
            q->last = NULL;

        return temp;
    }
}

bool is_empty(struct queue *q)
{
    return (q->first == NULL);
}

int djikstra(int g[][10000], int s, int d, int len)
{
    int distances[len];
    int current, current_distance, tentative;

    struct queue *q = create_queue();
    struct node *temp;

    for (int i = 0; i < len; i++)
    {
        distances[i] = 65535;
    }

    distances[s - 1] = 0;

    enqueue(q, s, distances[s - 1]);

    while (!(is_empty(q)))
    {
        temp = dequeue(q);
        current = temp->vertex;
        current_distance = temp->distance;
        ;
        if (current_distance > distances[current - 1])
            continue;

        for (int i = 1; i <= len; i++)
        {
            if (g[current - 1][i - 1] > 0)
            {
                tentative = distances[current - 1] + g[current - 1][i - 1];
                if (tentative < distances[i - 1])
                {
                    distances[i - 1] = tentative;
                    enqueue(q, i, tentative);
                }
            }
        }
    }

    return distances[d - 1];
}

int main()
{
    int i, j, n, a, b, v1, v2, w;
    std::cin >> n >> a >> b;

    int g[n][10000];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
            g[i][j] = 0;
    }

    for (i = 1; i < n; i++)
    {
        std::cin >> v1 >> v2 >> w;
        g[v1 - 1][v2 - 1] = w;
        g[v2 - 1][v1 - 1] = w;
    }
    std::cout << djikstra(g, a, b, n) << std::endl;
}