# Документация для кода

## setupStoreRoutes

```typescript
export const setupStoreRoutes = (server: ServerApp): void => {
  server.post('/store.buy', async (req, res) => {
    // Проверка входных данных
    const validated = storeBuyReqValidator.safeParse(req.body)
    if (!validated.success) {
      throw new UnauthorizedError('Что-то пошло не так')
    }

    const { goodId, itemType } = validated.data
    const userId = Number((req as UserRequest)[vkAuthSym])

    // Покупка флагов и цветов
    const user = await UserModel.findById(userId)
    if (!user) throw new NotFoundError('Пользователь не найден')
    if (itemType === 'flag') {
      await buyFlag(user, userId, goodId as IFlagName)
    }
    if (itemType === 'color') {
      await buyColor(user, userId, goodId as ICOLORNAME)
    }
    res.status(204)
  })

  server.post('/store.get', async (req, res) => {
    // Проверка входных данных
    const validated = storeGetReqValidator.safeParse(req.body)
    if (!validated.success) {
      throw new UnauthorizedError('Что-то пошло не так')
    }

    const isPointsFilter = req.body.filter === StoreFilters.All
    const isColorsFilter = req.body.filter === StoreFilters.Colors
    const isFlagsFilter = req.body.filter === StoreFilters.Flags

    // Получение флагов и цветов пользователя
    const [UserFlags, UserColors] = await Promise.all([
      FlagModel.find(
        {
          owner: (req as UserRequest)[vkAuthSym],
        },
        'flags'
      ),
      ColorModel.find(
        {
          owner: (req as UserRequest)[vkAuthSym],
        },
        'colors'
      ),
    ])

    // Получение исключенных цветов и флагов пользователя
    const excludedColors =
      UserColors[0]?.colors.filter(Boolean).map((color) => color.name) ?? []
    const excludedFlags = UserFlags[0]?.flags.map((flag) => flag.code) ?? []

    // Фильтрация доступных флагов и цветов
    const filteredFlags = Object.values(FlagCodes)
      .filter((code) => !excludedFlags.includes(code))
      .map((code) => {
        const name = Object.keys(FlagCodes).find(
          (key) => FlagCodes[key as keyof typeof FlagCodes] === code
        )
        return { name, code }
      })
    const filteredColors = Object.keys(ColorCodes).filter(
      (code) => !excludedColors.includes(code)
    )

    // Получение данных для каждого фильтра
    const [points, flags, colors] = await Promise.all([
      isPointsFilter && [{ donate: DONATE_POINTS } as DonateRes],
      isFlagsFilter && [{ flags: filteredFlags } as FlagRes],
      isColorsFilter && [{ colors: filteredColors } as ColorRes],
    ])

    // Составление списка элементов
    const items: StoreGetRes['items'] = [
      ...(points || []),
      ...(flags || []),
      ...(colors || []),
    ]
    res.send({ items })
  })
}
```

Этот код экспортирует функцию `setupStoreRoutes`, которая настраивает маршруты для работы с магазином. В этой функции определены два маршрута: `/store.buy` и `/store.get`.

### Маршрут `/store.buy`

Маршрут `/store.buy` обрабатывает POST-запросы и отвечает за покупку товаров в магазине. Входные данные должны быть проверены с помощью валидатора `storeBuyReqValidator`. Если данные не прошли проверку, будет выброшена ошибка `UnauthorizedError` с сообщением "Что-то пошло не так". После проверки данных происходит покупка флагов или цветов в зависимости от типа товара. Если тип товара - "flag", вызывается функция `buyFlag`, а если тип товара - "color", вызывается функция `buyColor`. Затем возвращается статус 204 (No Content).

### Маршрут `/store.get`

Маршрут `/store.get` также обрабатывает POST-запросы и отвечает за получение информации о доступных товарах в магазине. Входные данные должны быть проверены с помощью валидатора `storeGetReqValidator`. Если данные не прошли проверку, будет выброшена ошибка `UnauthorizedError` с сообщением "Что-то пошло не так". Затем происходит получение флагов и цветов пользователя. Далее определяются фильтры для отображения определенных типов товаров. Затем происходит фильтрация доступных флагов и цветов, исключая те, которые уже имеются у пользователя. Затем происходит получение данных для каждого фильтра. Наконец, составляется список элементов и отправляется в ответ.