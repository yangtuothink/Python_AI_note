"""
User
    username        varchar ( 64 )      u
    pwd             varchar ( 16 )      u
    email           email       null
    date            date        date()
    phone           int         null
    vip             int         default(0)
    pay             varchar( 16 )

Production
    title           varchar ( 64 )      u
    price           int
    last            int
    info            varchar ( 128 )      u
    comments        fk       Comments
    base_img             varchar ( 64 )
    detail_img      fk          Img
    video           varchar ( 64 )
    detail          varchar ( 64 )

Img
    img           varchar ( 64 )

Comment
    level           int
    user_id         fk      User
    date            auto        (  )
    like            int         ( 点赞 )
    content         varchar ( 255 )

Order
    user_id        fk    User
    date
    prd_id         fk     Production
    money          int
    pay            varchar( 16 )
    status         int

history
    user_id         fk      User
    pro_id          fk      Production

Shopping_car
    user_id         fk      User
    pro_id          fk      Production
    img_id          fk      Production_img


















"""






