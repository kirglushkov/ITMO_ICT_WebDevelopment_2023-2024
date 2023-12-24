# Документация для кода

В этом документе представлен код на языке JavaScript, который использует библиотеку `@vkontakte/vkui` для создания интерфейса пользователя. Код также использует компоненты `ActionButton` и `Title` из библиотеки `@/components`.

## Импорт компонентов

```javascript
import ActionButton from '@/components/ActionButton'
import styled from '@emotion/styled'
import Title from '@/components/Title'
import { NavIdProps, Panel } from '@vkontakte/vkui'
```

В этой части кода мы импортируем компоненты `ActionButton`, `styled`, `Title`, `NavIdProps` и `Panel` из соответствующих модулей.

## Стилизация компонентов

```javascript
const ActionsStack = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
`

const Center = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 0 10px;

  margin-top: calc(30vh - 42px);
  z-index: 2;
`
```

Здесь мы определяем пользовательские стили для компонентов `ActionsStack` и `Center` с помощью библиотеки `styled`. Компонент `ActionsStack` отображает свои дочерние элементы в столбце с выравниванием по центру и промежутками между ними в 10 пикселей. Компонент `Center` отображает свои дочерние элементы в столбце с выравниванием по центру и промежутками между ними в 20 пикселей. Он также имеет отступ сверху, вычисленный на основе высоты окна минус 42 пикселя, и `z-index` равный 2.

## Компонент Home

```javascript
export const Home: FC<NavIdProps> = (props) => {
  return (
    <Panel {...props}>
      <Center>
        <Title>
          соедини <br /> 4
        </Title>
        <FourCircles />
        <ActionsStack>
          <ActionButton marginBottom={6} fontSize={32} pathTo="/waitroom">
            играть
          </ActionButton>
          {/* <ActionButton pathTo="/bonuses">получить бонус</ActionButton> */}
          <ActionButton pathTo="/rating">рейтинг</ActionButton>
          <ActionButton pathTo="/inventory">инвентарь</ActionButton>
          <ActionButton pathTo="/skills">скиллы</ActionButton>
        </ActionsStack>
      </Center>
    </Panel>
  )
}
```

Этот компонент `Home` является функциональным компонентом, который принимает пропсы типа `NavIdProps`. Он отображает панель с содержимым внутри компонента `Center`. Внутри `Center` мы отображаем компонент `Title`, который отображает текст "соедини" и "4" на двух разных строках. Затем мы отображаем компонент `FourCircles`, который не определен в данном коде. Далее мы отображаем компонент `ActionsStack`, который содержит несколько компонентов `ActionButton`. Каждый `ActionButton` имеет свои собственные пропсы, такие как `marginBottom`, `fontSize` и `pathTo`, которые задают отступ снизу, размер шрифта и путь для перехода при нажатии на кнопку соответственно.

Это основной код, который отображает интерфейс пользователя на странице.