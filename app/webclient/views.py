from django.shortcuts import render


def home(request):
    context={
        "next_events":[
            {"name":"Pujada Formentor", "id":1, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/272468882_675485863606941_3767205089792939452_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=ONQ3fsb6VCsAX9tvJuP&_nc_ht=scontent-mad1-1.xx&oh=00_AfAMJwhoRJpZFkrePdyxiCLX5jGcX9WHYd0IcImwhijgzw&oe=63F3E2CB"},
            {"name":"I Meeting Karting Magaluf", "id":2, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/319901892_888123129009879_7662014948147052339_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=7g8wXTIn3SkAX8eVUmu&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfCtXFb-nozNw2sezONmHclKaR3B_PNk2Tf2J8RTlvuZOA&oe=63F3C6C1"},
            {"name":"I Autocross Felanitx", "id":3, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/311942029_852585112563681_8745874198094931107_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=ffbaGvDHR2oAX9ScH1F&_nc_ht=scontent-mad1-1.xx&oh=00_AfDEwAGKx5DEYkLPc_8NzbZPdK77b5ZbMPJrc0QfxIykeQ&oe=63F31024"},
            {"name":"Pujada Valldemosa", "id":4, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/322867118_636141138266016_5697471845099927385_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_ohc=uHJxULYzR0AAX_tl6UM&_nc_ht=scontent-mad1-1.xx&oh=00_AfBoUXMyiJOdF0k8OyEmZRU0HC0XZpWjNKJJIPhVz7PmBw&oe=63F2EE10"},
            {"name":"Rally Sol de Ponent", "id":5, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/274356600_692074258614768_6470898453832790499_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=Av4KJFKXrOAAX9ue2R2&_nc_ht=scontent-mad1-1.xx&oh=00_AfBcQQDUcUwIod_7sjfa0yboMruw4gjvawHnGjJllFrETQ&oe=63F296D8"},
        ],
        "rallyes":[
            {"name":"Sol de Ponent", "id":1, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/274356600_692074258614768_6470898453832790499_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=Av4KJFKXrOAAX9ue2R2&_nc_ht=scontent-mad1-1.xx&oh=00_AfBcQQDUcUwIod_7sjfa0yboMruw4gjvawHnGjJllFrETQ&oe=63F296D8"},
            {"name":"Rally clásico", "id":2, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/271507065_666642567824604_7918760817938678207_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=4ePVjHk_U9cAX96OyS5&_nc_ht=scontent-mad1-1.xx&oh=00_AfBKcrQChJVoMvfMzyjw9ZXGrt_4PN0RA0xDvZtY5yKzJg&oe=63F29847"},
            {"name":"Rallysprint Manacor", "id":3, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/274349883_692075935281267_770553665776950564_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=730e14&_nc_ohc=ucAcvPEhwfoAX-EOONb&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfDLC6aUnAV5CuBRLSShxZYpvtdujd9UzJoa1d3-tfI4Yg&oe=63F3E6D1"},
            {"name":"Ecorally", "id":4, "img":"https://uh.gsstatic.es/sfAttachPlugin/2254089.jpg"},
            {"name":"Rallysprint Mitja Illa", "id":5, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/298840997_551097283474897_2386788717039717630_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=e3f864&_nc_ohc=qY91RPxxkn0AX8IEahN&_nc_ht=scontent-mad1-1.xx&oh=00_AfCSLJJB7xUCbfJbN3pnz0-r4BOsAIZnirEU-Bc4mit_IA&oe=63F30188"},
            {"name":"Rallysprint Llucmajor", "id":6, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/278970928_730728184749375_7623902830046160728_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=BJX3CtIib54AX-_xX54&_nc_ht=scontent-mad1-1.xx&oh=00_AfAz_oXpM_Fm4ZG0h2thcwfX0k8T7cUqiiN75MLbqFxtoA&oe=63F30B6A"},
            {"name":"Rallysprint S'aficio", "id":7, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t1.18169-9/11095662_10205825930080755_2746151510436868543_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=cdbe9c&_nc_ohc=K2efEfIgucAAX9Su5Kw&_nc_ht=scontent-mad1-1.xx&oh=00_AfACHtRPqGdBrn243fVytvOh_FCrRll5yUIRnkpQ7IVqQA&oe=6415E953"},
            {"name":"Rally Vall de Sant Pere", "id":8, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/307937523_827335755088617_751573037868870928_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=8gl1zSVBOc8AX-nuFcA&_nc_ht=scontent-mad1-1.xx&oh=00_AfCSaPIchnlOn5bqZiPbLtPXhSJPyanPMnJgH26EO1ZEKg&oe=63F364E6"},
            {"name":"Rally Bunyola", "id":9, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/312659484_857627638726095_1767438774835957092_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_ohc=nco_b1oLezMAX-sCtD-&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfAe_kCsTjuoJtL2VIwj7VhSvBVSB0KQYDsA1eXfmyab5Q&oe=63F36679"},
            {"name":"Rally Chagenge 550", "id":10, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/311110684_841980473624145_6069147237828153483_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=CPLCSLHgmtwAX8ZEGtF&_nc_oc=AQm1a5nfh4uQRvIr1M-aAN88deL8VUet_a_Lh00K9e3TMd8CfWdEXvMUG40xhwuBbzE&_nc_ht=scontent-mad1-1.xx&oh=00_AfCHlM0MbPK37SgfcPE8UT-kIFCL9v9px-vbIJYb2CgMaQ&oe=63F384F3"},
            {"name":"Rally Dijous Bo", "id":11, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/315301706_867588197730039_6899158960450730644_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_ohc=80cpLbARHmYAX_TI2X6&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfB7DepCdi6rn7gA1tfvOhlyj7J1dmv5qD0TRyhpihmPbA&oe=63F40195"},
            {"name":"Rallysprint Conserves Rosselló", "id":12, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/316958878_877200416768817_4388235606927967586_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=m4izVvwAoEEAX9CWm3T&_nc_ht=scontent-mad1-1.xx&oh=00_AfBSwxWj7qYJP_R_TPMPAhiVvOinx6niux6q5UuNyBqs1Q&oe=63F2383E"},
            {"name":"Rallysprint Santanyí", "id":13, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/320808842_688525456136387_4255772736178536664_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=lcxhlaRHIr0AX-5OSBr&_nc_ht=scontent-mad1-1.xx&oh=00_AfCL7RTmVEg6gEJSY513n05QMsmZ0nqpgasNl47gKp1cQQ&oe=63F3F4D6"},
        ],
        "pujades":[
            {"name":"Formentor", "id":1, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/272468882_675485863606941_3767205089792939452_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=ONQ3fsb6VCsAX9tvJuP&_nc_ht=scontent-mad1-1.xx&oh=00_AfAMJwhoRJpZFkrePdyxiCLX5jGcX9WHYd0IcImwhijgzw&oe=63F3E2CB"},
            {"name":"Valldemosa", "id":2, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/322867118_636141138266016_5697471845099927385_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_ohc=uHJxULYzR0AAX_tl6UM&_nc_ht=scontent-mad1-1.xx&oh=00_AfBoUXMyiJOdF0k8OyEmZRU0HC0XZpWjNKJJIPhVz7PmBw&oe=63F2EE10"},
            {"name":"Aigües Blanques", "id":3, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/277763679_718553772633483_220998954764994438_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=730e14&_nc_ohc=GnlCUghOzaMAX9VclFw&_nc_ht=scontent-mad1-1.xx&oh=00_AfDjxQcQnwOYb_a9W3kJ4RerAJgnFoCN81o7bbhRM7s81g&oe=63F2949E"},
            {"name":"Puig Major Revival", "id":4, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/310845444_838780267277499_1252538450798951917_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=3jBJpfqlZwIAX_NZQWJ&_nc_ht=scontent-mad1-1.xx&oh=00_AfD3SrldelvpmQarDs9wO8l_4JI1G8oO1kwKhKqOC5WMQw&oe=63F33253"},
            {"name":"Sa Creu", "id":5, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/280103867_744343493387844_6218683097398357234_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=730e14&_nc_ohc=yQdZxIml2oIAX9ojJB9&_nc_ht=scontent-mad1-1.xx&oh=00_AfCSI3WDR8MW-QrrIv17Vml-qFdEwfJBg_Ga8Y8V-NHWlQ&oe=63F2EB77"},
            {"name":"Pollença-Lluc", "id":6, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/284194349_753291879159672_6039884186779472486_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_ohc=p-j8VqZaK6YAX8ehamw&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfDWbIvGzVjHtqWesJUgOZqvzYLtCr4sts_9hZBgBH_Ixw&oe=63F2C9BF"},
            {"name":"Son Mas", "id":7, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/291759516_777059830116210_9029988136876720866_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_ohc=y81HAiMgt-EAX-GM3Tp&_nc_ht=scontent-mad1-1.xx&oh=00_AfD1H3g9uyzLV4PynkWYPKF01egKgyaTFw76oRmDNleg2A&oe=63F313A1"},
            {"name":"San Salvador", "id":8, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/322185380_8539926399411211_6271081384736237560_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=730e14&_nc_ohc=ahgOPMAlaEcAX8-qvkH&_nc_ht=scontent-mad1-1.xx&oh=00_AfBXmuqgYzlDlWccaZtpIfd7v3DebZ70wTNqraRGbU3DVg&oe=63F3651B"},
            {"name":"Puig Major", "id":9, "img":"https://uh.gsstatic.es/deportes/motor/2022/09/29/2116141/cortes-trafico-motivo-pujada-puig-major.jpg"},
            {"name":"Sa Cala", "id":10, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t1.18169-9/304489_133799680099159_1594975744_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=cdbe9c&_nc_ohc=i3CgolR0tQ8AX-uM2KH&_nc_ht=scontent-mad1-1.xx&oh=00_AfB3itKPCa5HKk_u9HclYwk7EvNaKD0LavLVKnezE3HaDQ&oe=6415DF8E"},
            {"name":"Puig Punyent-Galilea", "id":11, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/284033746_751133042708889_2656966443226194422_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_ohc=oww8MyBRJdcAX9UfUF4&_nc_ht=scontent-mad1-1.xx&oh=00_AfBCgLoAbBBwhldg_-wuwDOr2tMjL0hwh-3wKJkSfR6qeg&oe=63F29D76"},
        ],
            "karting":[
            {"name":"I Meeting Karting Circuito Magaluf", "id":1, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/319901892_888123129009879_7662014948147052339_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=7g8wXTIn3SkAX8eVUmu&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfCtXFb-nozNw2sezONmHclKaR3B_PNk2Tf2J8RTlvuZOA&oe=63F3C6C1"},
            {"name":"II Meeting Karting Circuito Can Picafort", "id":2, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/319654729_888119025676956_4855225983715731477_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=JuOADUMf9TUAX-YQu9W&_nc_ht=scontent-mad1-1.xx&oh=00_AfBFAFEP-1EVyIUE4ZBMF6TpIispwVAzV8J92apHnoPRJw&oe=63F27A17"},
            {"name":"III Meeting Karting Circuito a determinar", "id":3, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/326837444_1238055127115126_7314373793561279047_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_ohc=aWC4cVWPYskAX8L2yHM&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfAl-mVnXRZ6Yn07GXLJ87isIVDdGq_3GVbwzTPDt5OKVA&oe=63F31268"},
            {"name":"IV Meeting Karting Circuito Magaluf (nocturna)", "id":4, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/316524030_873048320517360_5871073587280808892_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=730e14&_nc_ohc=mWzwO-yo1WAAX8iN_E-&_nc_ht=scontent-mad1-1.xx&oh=00_AfAT0n1__39XW6MxYNfPSmit5EiyAbasDkn_ut_hBlbyEg&oe=63F25384"},
            {"name":"V Meeting Karting Circuito Can Picafort ", "id":5, "img":"https://cdn1.yumping.com/emp/fotos/1/2/5/9/tb_e-1259-al-volante-del-kart-en-el-circuito16260916444078.jpg"},
            {"name":"VI Meeting Karting Circuito Magaluf", "id":6, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/273991058_688437908978403_6998470101806749667_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=730e14&_nc_ohc=p3_b2TKB4S8AX_OyXd8&_nc_ht=scontent-mad1-1.xx&oh=00_AfA79kUoB5QwH9CBuyKZVjSAXgov4um0kD2kz0ICje0jgw&oe=63F39EE9"},
        ],
            "autocross":[
            {"name":"I Autocross Felanitx ", "id":1, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/311942029_852585112563681_8745874198094931107_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=ffbaGvDHR2oAX9ScH1F&_nc_ht=scontent-mad1-1.xx&oh=00_AfDEwAGKx5DEYkLPc_8NzbZPdK77b5ZbMPJrc0QfxIykeQ&oe=63F31024"},
            {"name":"II Autocross Felanitx", "id":2, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/273042814_680007196488141_10711735578380692_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_ohc=9c6-laROj8AAX-nAQsj&_nc_ht=scontent-mad1-1.xx&oh=00_AfAFHXreNxeI6VIZ144remzi6tIhvUkFMaTBr0hKnmTCWg&oe=63F37F5B"},
            {"name":"Autocross festes de Sant Jordi (Eivissa)", "id":3, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/273043298_680006669821527_3322327249006688336_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=8AUxFo-kQgUAX_yZB_5&tn=fxJAQeLD1LUyzQHn&_nc_ht=scontent-mad1-1.xx&oh=00_AfC6KBTXueoEVEif3MZqv0W9VZjZJPqCTBtlGNjeON3N1Q&oe=63F3FA38"},
            {"name":"Resistencia Autocross Felanitx", "id":4, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/326875406_1640506183074738_1865350547578393049_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=1FNM_4h7_pwAX8qXU2l&_nc_ht=scontent-mad1-1.xx&oh=00_AfCHciKOdwhNM4loil2B5JlXrO_oxs6cuy1DK7Okut4fiA&oe=63F39156"},
            {"name":"III Autocross Felanitx", "id":5, "img":"https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/311571797_852584995897026_8306111563693988198_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_ohc=5Vk7T_KtAJYAX8MlSqq&_nc_ht=scontent-mad1-1.xx&oh=00_AfA0WAs2OHnZWdnnW_8MlN4RMu741ijCc3cZ_3zWaIZYGQ&oe=63F2DB85"},
            {"name":"IV Autocross Felanitx", "id":6, "img":"https://www.cronicabalear.es/access/public/img/noticias/upload/4_1670180516.jpg"},
        ],
    }
    return render(request, 'home.html', context)
