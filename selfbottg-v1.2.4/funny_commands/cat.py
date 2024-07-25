import random

list_cats_img_url = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrIWTxnYVT6Ud85YKXi-gaJfbAJac4CiGVig&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4Uq53HrkUPFFbTiVOSSH_zreqJIUFYQO3TA&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX2IsxhghYbp5ylrRt0oUiOTUHws5w1rz7Tg&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrIWTxnYVT6Ud85YKXi-gaJfbAJac4CiGVig&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKHbIFWFmKm0nVYZchc0UN75s4TsE-3paI1NGE6xPZX4li3ffQeqvoX7ex6zwYFes85GU&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQr5QZGUrpUDumzatbBcMCJ33EsMcHLYyNdAA&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwkf7Ga1ognkSeYf0Rq0-WTuOzIieKqy0lYA&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKNZcK4b9qnjvI7dFFgOhwv4YqW0aEVHNV3w&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2lMp-ahTd7tRaO76N6UfvHMIKPlalkTg0-g&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWPlngfEjllG2HkuCbIxQm0Iukl5mpEZ_ggrHbK5IzMWMVCN0LJDhPPF6t_gYhkfYfOYI&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp5PZUnLrZOLChomvG5yJYxxm-DIIrFf212fUAKwSnRZahxPWCp0dpUJOZyL1Il41eThE&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLgvDnw1SqiAsPaGtkboAoApHBySntruZUn4NEaJucbmdHIVyb6a8lNqHZKWMT_fEcnMY&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyMLxuvNy9V8XFsAcDvmHHKomofaMZ2tb4skdLguK0bAOZg-Wq7ZN9qw-cnXTbiXRVWYk&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR11T4pto40Vrc5EbI3-hsk_T9NOeSlgCDojD8OLpWlqgbNTPvgvFqAZiZ2vj5WnOT3irs&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIVDVrtBFPBu88rduBzocWx3XqzkbbtbmYzEgjOX5prXR4gXN4HIhMzM4WhYhF3cN5VpA&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj_pfQjAKtj1gLZQJMu9q48-y3wMiCK6EcMQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsIVS_Vt5TyHABNiLWT_kg3z68K2T8sClFJQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVgxV7QEXMWHSx8DLW136yztEObcqENouMew&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR13H_IxuAi0TczFtSQtmlc5ES6V0XpK1S1tQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCiXapz8YbmpOoU49UkL4BHqqWbcRxcdp5_w&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPxBnEjuJVJrrIZs3Y4zxwgCDWIcR-G45gLEU8fF-iMF_QQV1o4S783Tc8OSgGBhCqRac&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLr0VbHfWymxH56RryXHIX6yIWQQ6JSlyTIA&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWCbWrvJ1_izqPWfQLddE6i8sE-BK4is_s8GOjEwnPdFdwdx9DoTHnfhCxz5WYq9lxRPk&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrMU7j-LMpTeMQiuVd59SugJpcJLDM6-Swrb31Zppu_5LJdFIpxVFuPE9LhKDbJKcqR2I&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc9qRdgzuyzFZh_yiPts0GMSbrH5SP4bXZeb4NAdEbYSMq1lYYTDklNlFUx2hh0PWldN8&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpUzLqUrmsIdcAiGIUrCFLOPIZLPjBWqD9n8pVnuSqGsRYhOXRTqlcJavklxyOBHaatog&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTITxkQBhQqMZ4nbzSDtGecRqycyT21XQyxgMfavL9KugFluMuSg_i-Mglpgcd1w4XgR0Q&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVDwfqFEsfVcec2d6yC0BQKnZb0soGaomQ6T4mRiKDkjXGJnXfS9ySQlNJEfcgGiSdYUM&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL76VzNiDxn4Kyb-ITux1l61IGTv2WHkncYHw5xtJz9EJYRch42MsxkX6JUNVKLAPUmIQ&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt_zO4mdLASX8dqTs-065RrjIdBZQqlS0UQtQCHRN_LyJ62g4aiaPD0hSCMIeKBWw4rIo&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQs1gsckoHIOIvYctl8j6Pyd5Gawvk5mSNrVigDmNob2tVkkqTCO9FQ0Pmp6DYkqWemYg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW8DUUjKp7pInrG5Ot2Kza_H1dndeOgaG9CMo7PwOhmwJewdhM18IqrT3zPGLxZJlXGO4&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWrzh8ExAhlAG2tqDXOvwpFOdGUrl3oCXppvm_kh8J0f6DsdnWflkJ9Rknc4uYQIJVQy0&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS_C20RF3IU_BLshe2XvzZN8t11lgrtz2cQUwT6M4QVzpbJcw-kh-xsdBrrsiwCGMoFnc&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSARWcGsyh1jhw6QiNtAs-nl2g5ZtV2owmtFQZ4banh_PJTq6TY47XYxEEqJRugodJywBM&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_cjGe4aK7FnGJsC7ORLc6N3nyyReRwUCeCyljOH1xHnylHNM30yABLKIk4qS_j1a7-Lg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQQpA1CuhbweiM1MWbFbo7KKjVGtxg5h-JM_iMprXVhxOnSTqpnP_h9d29GorRryVXots&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0Cv-xUZlYw6kA22aVJLUTpGT_35pQvgD0o8vV2n0nsL6vD4gz_KHAVF0YHj9tE9oEAhU&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2TM7RW0vx7EvP986fJFbXAvv86P5Jbq9BgQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVc7r2N6-p53xnypHcAcfVo72aXHRHTr9IAyZc_2TntATm22xSzTyHOx9OC0YYVpPsVkM&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS86nHyZuYsPrTpM2tYHMsDQyZ_fyRTBn7BXdrrmQ3rwF0BWncKRDIhoYwDilC09dAfESY&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCe0v9TXJy9AGHjuqtZGnZ6ptciRAIGuVFgqBNo_RzRu4pR9s1Ms_N_DtTLHYt07q13WU&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0l7ytUjyjZlacT_aoPybmGqMliOVujrCueQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzPULiZjMqiOSEsc36PXUf9vmtPdYA2tFU4F7H4MkEVaxjvrsicWB-xlb3gdEuv1g5n2c&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxA1gcCtzaWjuFH6uisfHfWbvJkHn6D8HadTWNl4XSdFFC30SNpnnJHt7hD-OwCeju4LI&usqp=CAU',
]

async def cat(client, message):
    await message.delete()
    await message.reply_photo(random.choice(list_cats_img_url))
    









