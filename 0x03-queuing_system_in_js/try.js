import { createCluster } from 'redis';

const cluster = createCluster({
    rootNodes: [
        {
            url: 'redis://127.0.0.1:16379'
        },
        {
            url: 'redis://127.0.0.1:16380'
        },
        // ...
    ]
});

cluster.on('error', (err) => console.log('Redis Cluster Error', err));

cluster.connect();

cluster.set('foo', 'bar');
const value = cluster.get('foo');
console.log(value); // returns 'bar'

cluster.quit();
