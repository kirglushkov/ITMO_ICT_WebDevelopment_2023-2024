# Отчёт по URL конфигурации Django проекта

Следующий список предоставляет информацию о путях (URLs), доступных в одном из приложений Django проекта. Каждый путь связан с соответствующим видом (view), который обрабатывает HTTP-запросы по этому адресу.

## Пути и Соответствующие Виды

1. **Стоимость по дате и доктору**
   - URL: `cost-by-date/`
   - Вид: `getCostByDateNDoctor`
   - Имя: `cost-by-date`

2. **Пациенты по дате**
   - URL: `patients-by-date/`
   - Вид: `getPatientsByDate`
   - Имя: `patients-by-date`

3. **Список оплативших пациентов**
   - URL: `list-patients-paid/`
   - Вид: `getListPatientsPaid`
   - Имя: `list-patients-paid`

4. **Доктора**
   - URL: `doctors/`
   - Вид: `getDoctors`
   - Имя: `doctors`

5. **Пациенты по имени доктора**
   - URL: `doctor-patients/`
   - Вид: `getPatientsbyDoctorName`
   - Имя: `doctor-patients`

6. **Количество пациентов оториноларинголога**
   - URL: `numbers-of-patients-otorhinolaryngologist/`
   - Вид: `getNumbersOfPatientsOtoronginolog`
   - Имя: `numbers-of-patients-otorhinolaryngologist`

7. **Доктор по дням**
   - URL: `doctor-by-day/`
   - Вид: `getDoctorByDay`
   - Имя: `doctor-by-day`

8. **Пациенты**
   - URL: `patients/`
   - Вид: `getPatients`
   - Имя: `patients`

9. **Отчёт о визите**
   - URL: `visit-report/`
   - Вид: `getVisitReport`
   - Имя: `visit-report`

В конце конфигурационного файла используется функция `format_suffix_patterns`, чтобы добавить поддержку форматированных суффиксов к каждому из URL путей.

```python
urlpatterns = format_suffix_patterns(urlpatterns)
```

Это позволяет клиентам запросить определённый тип контента, например JSON или HTML, используя префиксы, такие как `.json` или `.html` в конце URL пути.