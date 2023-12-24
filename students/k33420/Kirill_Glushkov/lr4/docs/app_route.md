## app.routes.ts

```typescript
import { ServerApp } from 'src'
import { setupTestRoutes } from './test.routes'
import { setupInventoryRoutes } from './inventory.routes'
import { setupStoreRoutes } from './store.routes'
import { setupUserRoutes } from './user.routes'
import { setupRatingRoutes } from './rating.routes'
import { setupFriendsRoutes } from './friends.routes'

export const setupAppRoutes = (server: ServerApp): void => {
  setupTestRoutes(server)
  setupInventoryRoutes(server)
  setupStoreRoutes(server)
  setupUserRoutes(server)
  setupRatingRoutes(server)
  setupFriendsRoutes(server)
}
```

This file `app.routes.ts` exports a function `setupAppRoutes` that accepts a `ServerApp` object as an argument. The function is responsible for setting up various routes by calling the respective setup functions from other files.

The imported modules are as follows:
- `ServerApp` from the `src` directory
- `setupTestRoutes` from `./test.routes`
- `setupInventoryRoutes` from `./inventory.routes`
- `setupStoreRoutes` from `./store.routes`
- `setupUserRoutes` from `./user.routes`
- `setupRatingRoutes` from `./rating.routes`
- `setupFriendsRoutes` from `./friends.routes`

The `setupAppRoutes` function sequentially calls each setup function with the `server` object as an argument. This ensures that all necessary routes are set up in the application.

Please note that the details of the setup functions are not provided in this file. To understand the implementation of each route setup, you need to refer to the respective files mentioned above.