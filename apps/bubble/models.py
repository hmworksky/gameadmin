# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BubbleAccountFlowLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    track_code = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=32)
    user_id = models.IntegerField()
    role_id = models.CharField(max_length=32)
    flow_id = models.CharField(max_length=32)
    coin_id = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=22, decimal_places=4)
    balance_type = models.IntegerField()
    first_order_no = models.CharField(max_length=32)
    total_balance = models.DecimalField(max_digits=22, decimal_places=4)
    avl_balance = models.DecimalField(max_digits=22, decimal_places=4)
    frozen_balance = models.DecimalField(max_digits=22, decimal_places=4)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_account_flow_log'


class BubbleActivity(models.Model):
    activity_num = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    prize = models.CharField(max_length=5000)
    type = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    price = models.DecimalField(max_digits=22, decimal_places=4)
    duration = models.BigIntegerField()
    rate = models.DecimalField(max_digits=22, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bubble_activity'


class BubbleActivityTaskRecord(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    track_u = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    raw_add_time = models.DateTimeField(blank=True, null=True)
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_activity_task_record'


class BubbleActivityUser(models.Model):
    user_id = models.IntegerField()
    activity_num = models.CharField(max_length=500)
    status = models.IntegerField()
    finish_date = models.DateField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_activity_user'


class BubbleCaifenPayMainFlow(models.Model):
    user_id = models.IntegerField()
    first_freezen_flow = models.CharField(max_length=100)
    latest_settlement_flow = models.CharField(max_length=100, blank=True, null=True)
    curr_available = models.DecimalField(max_digits=22, decimal_places=4)
    caipiao_order_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caifen_pay_main_flow'
        unique_together = (('user_id', 'first_freezen_flow'),)


class BubbleCaifenPayPlatformOrder(models.Model):
    user_id = models.IntegerField()
    first_freezen_flow = models.CharField(max_length=100)
    new_settlement_flow = models.CharField(unique=True, max_length=100)
    caipiao_order_id = models.CharField(max_length=100)
    game_settlement_flow = models.CharField(max_length=100, blank=True, null=True)
    caifen_amount = models.DecimalField(max_digits=22, decimal_places=4)
    flag = models.IntegerField()
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caifen_pay_platform_order'


class BubbleCaifenPayToSettle(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caifen_pay_to_settle'


class BubbleCaifenPayToSettleCopy(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    from_flow_id = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caifen_pay_to_settle_copy'


class BubbleCaifenPayToSettleFailed(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caifen_pay_to_settle_failed'


class BubbleCaijinPayMainFlow(models.Model):
    user_id = models.IntegerField()
    first_freezen_flow = models.CharField(max_length=100)
    latest_settlement_flow = models.CharField(max_length=100, blank=True, null=True)
    curr_available = models.DecimalField(max_digits=22, decimal_places=4)
    caipiao_order_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caijin_pay_main_flow'
        unique_together = (('user_id', 'first_freezen_flow'),)


class BubbleCaijinPayPlatformOrder(models.Model):
    user_id = models.IntegerField()
    first_freezen_flow = models.CharField(max_length=100)
    new_settlement_flow = models.CharField(unique=True, max_length=100)
    caipiao_order_id = models.CharField(max_length=100)
    game_settlement_flow = models.CharField(max_length=100, blank=True, null=True)
    caijin_amount = models.DecimalField(max_digits=22, decimal_places=4)
    flag = models.IntegerField()
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caijin_pay_platform_order'


class BubbleCaijinPayToSettle(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caijin_pay_to_settle'


class BubbleCaijinPayToSettleCopy(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    from_flow_id = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caijin_pay_to_settle_copy'


class BubbleCaijinPayToSettleFailed(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_caijin_pay_to_settle_failed'


class BubbleChapter(models.Model):
    chapter_num = models.CharField(unique=True, max_length=100)
    chapter_name = models.CharField(max_length=250)
    condition = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_chapter'


class BubbleChatFace(models.Model):
    face_num = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    type = models.IntegerField()
    display_order = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_chat_face'


class BubbleChatPreset(models.Model):
    chat_num = models.CharField(max_length=100)
    content = models.CharField(max_length=50)
    display_order = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_chat_preset'


class BubbleCheckpoint(models.Model):
    chapter_num = models.CharField(max_length=100)
    checkpoint_num = models.CharField(unique=True, max_length=100)
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    pass_value = models.CharField(max_length=300)
    boss_blood = models.IntegerField()
    boss_damage = models.IntegerField()
    boss_route = models.CharField(max_length=3000)
    boss_bubbles = models.CharField(max_length=5000)
    launch = models.CharField(max_length=3000)
    launch_num = models.IntegerField()
    panel = models.IntegerField()
    star_score = models.CharField(max_length=500)
    is_hard = models.IntegerField()
    pass_reward = models.CharField(max_length=1000)
    plot_num = models.CharField(max_length=100)
    plot_position = models.IntegerField()
    activity_num = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_checkpoint'


class BubbleCheckpointBubbles(models.Model):
    checkpoint_num = models.CharField(max_length=100)
    launch = models.CharField(max_length=3000)
    ghost_position = models.CharField(max_length=1000)
    bubbles = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_checkpoint_bubbles'


class BubbleConfig(models.Model):
    config_key = models.CharField(unique=True, max_length=100)
    config_value = models.CharField(max_length=5000)
    type = models.IntegerField()
    comment = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_config'


class BubbleDiscountPackage(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_discount_package'


class BubbleDiscountsItem(models.Model):
    discounts_list = models.CharField(max_length=5000)
    template_id = models.IntegerField()
    display_day = models.DateField(unique=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_discounts_item'


class BubbleDiscountsTemplate(models.Model):
    name = models.CharField(max_length=100)
    package = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_discounts_template'


class BubbleEggPoolLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    round_key = models.CharField(max_length=255)
    pool_customize_key = models.CharField(max_length=100)
    outer_flow_no = models.CharField(max_length=255)
    flow_no = models.CharField(max_length=255)
    type = models.IntegerField()
    status = models.IntegerField()
    ratio = models.DecimalField(max_digits=22, decimal_places=4)
    egg_amount = models.DecimalField(max_digits=22, decimal_places=4)
    egg_pool = models.DecimalField(max_digits=22, decimal_places=4)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_egg_pool_log'


class BubbleFillFlow(models.Model):
    user_id = models.IntegerField()
    currency_type = models.IntegerField()
    inner_flow_no = models.CharField(unique=True, max_length=50)
    return_order = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=22, decimal_places=4)
    retry_times = models.IntegerField()
    status = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_fill_flow'


class BubbleFlowLog(models.Model):
    platform = models.CharField(max_length=20)
    truck_code = models.CharField(max_length=100)
    channel_id = models.IntegerField()
    game_id = models.IntegerField()
    user_id = models.IntegerField()
    flow_id = models.CharField(max_length=32)
    out_flow_id = models.CharField(max_length=50)
    type = models.IntegerField()
    amount = models.DecimalField(max_digits=22, decimal_places=4)
    wlt = models.DecimalField(max_digits=22, decimal_places=4)
    td = models.DecimalField(max_digits=22, decimal_places=4)
    tb = models.DecimalField(max_digits=22, decimal_places=4)
    remain_wlt = models.DecimalField(max_digits=22, decimal_places=4)
    remain_td = models.DecimalField(max_digits=22, decimal_places=4)
    remain_tb = models.DecimalField(max_digits=22, decimal_places=4)
    freeze_wlt = models.DecimalField(max_digits=22, decimal_places=4)
    freeze_td = models.DecimalField(max_digits=22, decimal_places=4)
    freeze_tb = models.DecimalField(max_digits=22, decimal_places=4)
    caijin = models.DecimalField(max_digits=22, decimal_places=4)
    tingdou = models.DecimalField(max_digits=22, decimal_places=4)
    remain_caijin = models.DecimalField(max_digits=22, decimal_places=4)
    remain_tingdou = models.DecimalField(max_digits=22, decimal_places=4)
    freeze_caijin = models.DecimalField(max_digits=22, decimal_places=4)
    freeze_tingdou = models.DecimalField(max_digits=22, decimal_places=4)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_flow_log'


class BubbleFriendEnergy(models.Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
    energy = models.IntegerField()
    status = models.IntegerField()
    flow_id = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    expire_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_friend_energy'


class BubbleGameAccountChangeLog(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    deal_batch_flag = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    type = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_change_log'


class BubbleGameAccountDetail0(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_0'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail1(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_1'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail10(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_10'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail11(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_11'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail12(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_12'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail13(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_13'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail14(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_14'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail15(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_15'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail2(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_2'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail3(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_3'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail4(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_4'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail5(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_5'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail6(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_6'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail7(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_7'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail8(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_8'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountDetail9(models.Model):
    user_id = models.IntegerField()
    cust_id = models.IntegerField()
    game_id = models.IntegerField()
    account_type = models.IntegerField()
    amount_available = models.DecimalField(max_digits=22, decimal_places=4)
    amount_locked = models.DecimalField(max_digits=22, decimal_places=4)
    version = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_detail_9'
        unique_together = (('user_id', 'game_id', 'account_type'),)


class BubbleGameAccountFlow0(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_0'


class BubbleGameAccountFlow1(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_1'


class BubbleGameAccountFlow10(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_10'


class BubbleGameAccountFlow11(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_11'


class BubbleGameAccountFlow12(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_12'


class BubbleGameAccountFlow13(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_13'


class BubbleGameAccountFlow14(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_14'


class BubbleGameAccountFlow15(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_15'


class BubbleGameAccountFlow2(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_2'


class BubbleGameAccountFlow3(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_3'


class BubbleGameAccountFlow4(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_4'


class BubbleGameAccountFlow5(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_5'


class BubbleGameAccountFlow6(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_6'


class BubbleGameAccountFlow7(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_7'


class BubbleGameAccountFlow8(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_8'


class BubbleGameAccountFlow9(models.Model):
    flow_no = models.CharField(unique=True, max_length=50)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    operation_type = models.IntegerField()
    operation_flag = models.IntegerField()
    param = models.CharField(max_length=2000, blank=True, null=True)
    ext = models.CharField(max_length=1000, blank=True, null=True)
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_flow_9'


class BubbleGameAccountLog0(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_0'


class BubbleGameAccountLog1(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_1'


class BubbleGameAccountLog10(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_10'


class BubbleGameAccountLog11(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_11'


class BubbleGameAccountLog12(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_12'


class BubbleGameAccountLog13(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_13'


class BubbleGameAccountLog14(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_14'


class BubbleGameAccountLog15(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_15'


class BubbleGameAccountLog2(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_2'


class BubbleGameAccountLog3(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_3'


class BubbleGameAccountLog4(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_4'


class BubbleGameAccountLog5(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_5'


class BubbleGameAccountLog6(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_6'


class BubbleGameAccountLog7(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_7'


class BubbleGameAccountLog8(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_8'


class BubbleGameAccountLog9(models.Model):
    user_id = models.IntegerField()
    flow_no = models.CharField(max_length=255)
    game_account_id = models.IntegerField()
    add_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    subtract_value = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    curr_value = models.DecimalField(max_digits=22, decimal_places=4)
    remark = models.CharField(max_length=255, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_game_account_log_9'


class BubbleGoods(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_name = models.CharField(max_length=100)
    goods_num = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=22, decimal_places=4)
    goods = models.CharField(max_length=1000)
    delete_flag = models.IntegerField()
    extra_goods = models.CharField(max_length=1000)
    rebate_gold = models.CharField(max_length=1000)
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_goods'


class BubbleItem(models.Model):
    item_num = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    type = models.IntegerField()
    price = models.DecimalField(max_digits=22, decimal_places=4)
    item_cd = models.IntegerField()
    desc = models.CharField(max_length=5000)
    sort = models.IntegerField()
    is_display = models.IntegerField()
    activity_id = models.IntegerField()
    quality = models.IntegerField()
    persist = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    per_buy_count = models.IntegerField()
    phase = models.CharField(max_length=1000)
    checkpoint_num = models.CharField(max_length=100)
    use_limit = models.IntegerField()
    gold_price = models.DecimalField(max_digits=22, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'bubble_item'


class BubbleItemBuyLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    item_num = models.CharField(max_length=100)
    round_key = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=22, decimal_places=4)
    discounted_price = models.DecimalField(max_digits=22, decimal_places=4)
    num = models.IntegerField()
    type = models.IntegerField()
    flow_no = models.CharField(max_length=100)
    is_discounts = models.IntegerField()
    is_first = models.IntegerField()
    buy_date = models.DateField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=22, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'bubble_item_buy_log'


class BubbleItemUseLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    item_num = models.CharField(max_length=500)
    round_key = models.CharField(max_length=100)
    room_id = models.IntegerField()
    type = models.IntegerField()
    skill_num = models.IntegerField()
    item_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_item_use_log'


class BubbleJavaError(models.Model):
    params = models.CharField(max_length=5000)
    interface = models.CharField(max_length=500)
    return_data = models.CharField(max_length=1000)
    retry = models.IntegerField()
    is_success = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_java_error'


class BubbleLevelExpConfig(models.Model):
    level = models.IntegerField()
    type = models.IntegerField()
    min = models.BigIntegerField()
    name = models.CharField(max_length=50)
    max = models.BigIntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_level_exp_config'


class BubbleLoadingTips(models.Model):
    content = models.CharField(max_length=50)
    weight = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_loading_tips'


class BubbleMatchLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_match_log'


class BubbleMedal(models.Model):
    medal_num = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=250)
    info = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    phase = models.CharField(max_length=1000)
    reward = models.CharField(max_length=3000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_medal'


class BubbleMode(models.Model):
    name = models.CharField(max_length=500)
    type = models.SmallIntegerField(unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    config = models.CharField(max_length=5000)
    show_start_time = models.IntegerField()
    sort = models.IntegerField()
    is_display = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_mode'


class BubbleNewbie(models.Model):
    step = models.IntegerField(unique=True)
    name = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_newbie'


class BubbleNewbieLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    step = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_newbie_log'
        unique_together = (('user_id', 'step'),)


class BubbleOnlineStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    online_count = models.IntegerField()
    add_time = models.DateTimeField(unique=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_online_statistics'


class BubblePlot(models.Model):
    plot_num = models.CharField(unique=True, max_length=100)
    plot_memo = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_plot'


class BubblePoolLine(models.Model):
    amount = models.IntegerField()
    name = models.CharField(max_length=500)
    config = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_pool_line'


class BubbleRedPoint(models.Model):
    user_id = models.IntegerField(unique=True)
    content = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_red_point'


class BubbleRobot(models.Model):
    user_id = models.IntegerField()
    init_exp = models.IntegerField()
    exp = models.IntegerField()
    ai = models.IntegerField()
    max_second = models.IntegerField()
    item_use_freq = models.DecimalField(max_digits=22, decimal_places=4)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    use_item_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bubble_robot'


class BubbleRoom(models.Model):
    mode_type = models.IntegerField()
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    config = models.CharField(max_length=5000)
    sort = models.SmallIntegerField()
    entry_fee = models.DecimalField(max_digits=22, decimal_places=4)
    bubble_score = models.IntegerField()
    level = models.IntegerField()
    is_display = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_room'


class BubbleRound(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_id = models.IntegerField()
    round_key = models.CharField(unique=True, max_length=32)
    entry_fee = models.DecimalField(max_digits=20, decimal_places=4)
    service_rate = models.DecimalField(max_digits=22, decimal_places=4)
    status = models.IntegerField()
    duration = models.IntegerField()
    egg_pool = models.DecimalField(max_digits=22, decimal_places=4)
    is_egg = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_round'


class BubbleSkill(models.Model):
    skill_num = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=255)
    quality = models.IntegerField()
    memo = models.CharField(max_length=3000)
    intro = models.CharField(max_length=3000)
    energy = models.SmallIntegerField()
    sort = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_skill'


class BubbleSkillItem(models.Model):
    skill_num = models.CharField(max_length=100)
    item_num = models.CharField(unique=True, max_length=100)
    consume_item_config = models.CharField(max_length=5000)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_skill_item'
        unique_together = (('skill_num', 'item_num'),)


class BubbleSkillUseLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    skill_num = models.CharField(max_length=500)
    user_id = models.IntegerField()
    round_key = models.CharField(max_length=100)
    room_id = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_skill_use_log'


class BubbleStrengthLog(models.Model):
    user_id = models.PositiveIntegerField()
    strength = models.IntegerField()
    change_before = models.IntegerField()
    change_after = models.IntegerField()
    type = models.IntegerField()
    num = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_strength_log'


class BubbleTingdouPayMainFlow(models.Model):
    user_id = models.IntegerField()
    first_freezen_flow = models.CharField(max_length=100)
    latest_settlement_flow = models.CharField(max_length=100, blank=True, null=True)
    curr_available = models.DecimalField(max_digits=22, decimal_places=4)
    tingdou_flow_no = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    track_code = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tingdou_pay_main_flow'
        unique_together = (('user_id', 'first_freezen_flow'),)


class BubbleTingdouPayToSettle(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tingdou_pay_to_settle'


class BubbleTingdouPayToSettleCopy(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    from_flow_id = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tingdou_pay_to_settle_copy'


class BubbleTingdouPayToSettleFailed(models.Model):
    user_id = models.IntegerField()
    consume_amount = models.DecimalField(max_digits=22, decimal_places=4)
    settled_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tingdou_pay_to_settle_failed'


class BubbleTrackingInterface(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    open = models.BigIntegerField()
    add_date = models.DateField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tracking_interface'


class BubbleTrackingMode(models.Model):
    id = models.BigAutoField(primary_key=True)
    mode_type = models.IntegerField()
    open = models.BigIntegerField()
    match = models.BigIntegerField()
    join = models.BigIntegerField()
    skill_info = models.CharField(max_length=200)
    item_info = models.CharField(max_length=500)
    egg = models.BigIntegerField()
    add_date = models.DateField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tracking_mode'


class BubbleTrackingShop(models.Model):
    id = models.BigAutoField(primary_key=True)
    open = models.BigIntegerField()
    transaction = models.BigIntegerField()
    discount = models.BigIntegerField()
    add_date = models.DateField(unique=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tracking_shop'


class BubbleTrackingSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    open = models.BigIntegerField()
    singe_active = models.BigIntegerField()
    permanent_active = models.BigIntegerField()
    change = models.BigIntegerField()
    add_date = models.DateField(unique=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tracking_skill'


class BubbleTrackingSkin(models.Model):
    id = models.BigAutoField(primary_key=True)
    open = models.BigIntegerField()
    change = models.BigIntegerField()
    add_date = models.DateField(unique=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tracking_skin'


class BubbleTrackingTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    open = models.BigIntegerField()
    jump = models.BigIntegerField()
    add_date = models.DateField(unique=True)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_tracking_task'


class BubbleUserAccount(models.Model):
    user_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=100)
    user_type = models.IntegerField()
    match_level = models.BigIntegerField()
    room_streak = models.CharField(max_length=1000)
    icon = models.CharField(max_length=255)
    exp = models.IntegerField()
    win_amount = models.DecimalField(max_digits=22, decimal_places=4)
    bet_amount = models.DecimalField(max_digits=22, decimal_places=4)
    total_count = models.IntegerField()
    win_count = models.IntegerField()
    lose_count = models.IntegerField()
    tie_count = models.IntegerField()
    login_time = models.DateTimeField()
    status = models.IntegerField()
    newbie_step = models.IntegerField()
    is_robot = models.IntegerField()
    is_new = models.IntegerField()
    strength = models.IntegerField()
    recover_time = models.DateTimeField()
    consume_time = models.DateTimeField()
    chapter_num = models.IntegerField()
    checkpoint_num = models.IntegerField()
    pve_stars = models.IntegerField()
    pve_use_skill_count = models.IntegerField()
    pve_cumulate_eliminate_count = models.BigIntegerField()
    pve_score = models.BigIntegerField()
    pve_balance_auto = models.IntegerField()
    giving_strength_count = models.IntegerField()
    plat_amount = models.DecimalField(max_digits=22, decimal_places=4)
    gold_amount = models.DecimalField(max_digits=22, decimal_places=4)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    unlimited_time_remaining = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_account'


class BubbleUserChapterLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    chapter_num = models.CharField(max_length=100)
    first_pass_condition = models.IntegerField()
    unlock_gold = models.DecimalField(max_digits=22, decimal_places=4)
    share_count = models.IntegerField()
    star_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_chapter_log'


class BubbleUserCheckpoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    chapter_num = models.CharField(max_length=100)
    checkpoint_num = models.CharField(max_length=100)
    is_pass = models.IntegerField()
    is_pass_plot = models.IntegerField()
    stars = models.IntegerField()
    score = models.BigIntegerField()
    is_first = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_checkpoint'


class BubbleUserCheckpointLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    chapter_num = models.CharField(max_length=100)
    checkpoint_num = models.CharField(max_length=100)
    strength = models.IntegerField()
    score = models.IntegerField()
    launch_step = models.IntegerField()
    is_pass = models.IntegerField()
    pass_stars = models.IntegerField()
    status = models.IntegerField()
    skill_info = models.CharField(max_length=3000)
    item_info = models.CharField(max_length=3000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_checkpoint_log'


class BubbleUserConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    config_key = models.CharField(max_length=100)
    type = models.IntegerField()
    config_value = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_config'
        unique_together = (('user_id', 'config_key'),)


class BubbleUserDayRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    next_day_retain = models.DecimalField(max_digits=22, decimal_places=6)
    three_days_retain = models.DecimalField(max_digits=22, decimal_places=6)
    seven_days_reatin = models.DecimalField(max_digits=22, decimal_places=6)
    fourteen_days_reatin = models.DecimalField(max_digits=22, decimal_places=6)
    thirty_days_reatin = models.DecimalField(max_digits=22, decimal_places=6)
    login_total = models.IntegerField()
    login_user_num = models.IntegerField()
    new_user_num = models.IntegerField()
    pay_user_num = models.IntegerField()
    pay_total = models.DecimalField(max_digits=22, decimal_places=2)
    user_total = models.IntegerField()
    pve_total = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_day_record'


class BubbleUserExpLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    round_key = models.CharField(max_length=200)
    exp = models.IntegerField()
    field_type = models.IntegerField(db_column=' type')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_exp_log'


class BubbleUserFreeze(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    amount = models.DecimalField(max_digits=22, decimal_places=4)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    memo = models.CharField(max_length=255)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_freeze'


class BubbleUserItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    item_num = models.CharField(max_length=100)
    item_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_item'
        unique_together = (('user_id', 'item_num'),)


class BubbleUserMedal(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    medal_num = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    count = models.BigIntegerField()
    is_all_receive = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_medal'


class BubbleUserMedalLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    medal_num = models.CharField(max_length=100)
    phase = models.IntegerField()
    reward = models.CharField(max_length=1000)
    status = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_medal_log'


class BubbleUserModeStatistics(models.Model):
    mode_type = models.IntegerField()
    user_id = models.IntegerField()
    bet_amount = models.DecimalField(max_digits=22, decimal_places=4)
    win_amount = models.DecimalField(max_digits=22, decimal_places=4)
    total_count = models.IntegerField()
    win_count = models.IntegerField()
    lose_count = models.IntegerField()
    tie_count = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_mode_statistics'
        unique_together = (('user_id', 'mode_type'),)


class BubbleUserMonthRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    month_retain = models.DecimalField(max_digits=22, decimal_places=6)
    login_total = models.IntegerField()
    login_user_num = models.IntegerField()
    new_user_num = models.IntegerField()
    pay_user_num = models.IntegerField()
    pay_total = models.DecimalField(max_digits=22, decimal_places=2)
    user_total = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_month_record'


class BubbleUserOnline(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    socket_id = models.CharField(max_length=100)
    status = models.IntegerField()
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    online_time = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_online'
        unique_together = (('user_id', 'socket_id'),)


class BubbleUserOperateLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_id = models.IntegerField()
    round_key = models.CharField(max_length=100)
    user_id = models.IntegerField()
    is_robot = models.IntegerField()
    cmd = models.CharField(max_length=100)
    bubble_id = models.IntegerField()
    angle = models.IntegerField()
    path = models.CharField(max_length=2000)
    drop_bubbles = models.CharField(max_length=2000)
    eliminate = models.CharField(max_length=2000)
    land = models.CharField(max_length=5000)
    is_egg = models.IntegerField()
    panel = models.CharField(max_length=5000)
    crazy_score = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    skill_num = models.CharField(max_length=100)
    step = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bubble_user_operate_log'


class BubbleUserOrderInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    track_code = models.CharField(max_length=100)
    type = models.IntegerField()
    num = models.CharField(max_length=100)
    detail = models.CharField(max_length=3000)
    order_no = models.CharField(unique=True, max_length=100)
    order_amount = models.DecimalField(max_digits=22, decimal_places=4)
    gold_amount = models.DecimalField(max_digits=22, decimal_places=4)
    status = models.IntegerField()
    delete_flag = models.IntegerField()
    order_end_time = models.DateTimeField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_order_info'


class BubbleUserPrizeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    prize_type = models.IntegerField()
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=500)
    type = models.IntegerField()
    item_num = models.CharField(max_length=100)
    count = models.IntegerField()
    t_point = models.DecimalField(max_digits=22, decimal_places=4)
    get_date = models.DateField()
    extend = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_prize_log'


class BubbleUserRoundLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_id = models.IntegerField()
    round_key = models.CharField(max_length=32)
    user_id = models.IntegerField()
    track_code = models.CharField(max_length=500)
    win_amount = models.DecimalField(max_digits=22, decimal_places=4)
    profit_amount = models.DecimalField(max_digits=22, decimal_places=4)
    bet_amount = models.DecimalField(max_digits=22, decimal_places=4)
    pool_amount = models.DecimalField(max_digits=22, decimal_places=4)
    egg_amount = models.DecimalField(max_digits=22, decimal_places=4)
    lottery_amount = models.DecimalField(max_digits=22, decimal_places=4)
    skill_info = models.CharField(max_length=200)
    bet_rank = models.IntegerField()
    item_info = models.CharField(max_length=500)
    eliminate_info = models.CharField(max_length=1000)
    is_robot = models.IntegerField()
    status = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    pre_match_level = models.IntegerField()
    post_match_level = models.IntegerField()
    round_id = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'bubble_user_round_log'


class BubbleUserSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    skill_num = models.CharField(max_length=100)
    user_id = models.IntegerField()
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_skill'
        unique_together = (('user_id', 'skill_num'),)


class BubbleUserWeekRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    week_retain = models.DecimalField(max_digits=22, decimal_places=6)
    login_total = models.IntegerField()
    login_user_num = models.IntegerField()
    new_user_num = models.IntegerField()
    pay_user_num = models.IntegerField()
    pay_total = models.DecimalField(max_digits=22, decimal_places=2)
    user_total = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_user_week_record'


class BubbleWxShare(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    user_id = models.IntegerField()
    ext1 = models.DecimalField(max_digits=22, decimal_places=4)
    ext2 = models.CharField(max_length=1000)
    status = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bubble_wx_share'


class FriendApply(models.Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
    status = models.IntegerField()
    op_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'friend_apply'


class FriendBaseConfig(models.Model):
    key_name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'friend_base_config'


class FriendRelation(models.Model):
    friend_apply_id = models.IntegerField()
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'friend_relation'


class Mail(models.Model):
    mail_type = models.IntegerField()
    tag = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    attachment_type = models.IntegerField()
    send_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_check = models.IntegerField()
    strategy = models.CharField(max_length=255)
    extra_data = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail'


class MailAttchment(models.Model):
    mail_id = models.IntegerField()
    item_id = models.CharField(max_length=100)
    item_num = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_attchment'


class MailBaseConfig(models.Model):
    key_name = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_base_config'


class MailChoseAttach(models.Model):
    attachment_id = models.IntegerField()
    attachment_title = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_chose_attach'


class MailChoseAttachCopy(models.Model):
    attachment_id = models.IntegerField()
    attachment_title = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_chose_attach_copy'


class MailSubscribe(models.Model):
    mail_type = models.IntegerField()
    tag = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    attachment_type = models.IntegerField()
    send_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_check = models.IntegerField()
    strategy = models.CharField(max_length=255)
    extra_data = models.CharField(max_length=500)
    user_list = models.CharField(max_length=5000)
    attchment_list = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_subscribe'


class MailUser(models.Model):
    mail_type = models.IntegerField()
    mail_id = models.IntegerField()
    user_id = models.PositiveIntegerField()
    from_user_id = models.PositiveIntegerField()
    is_read = models.IntegerField()
    is_receive = models.IntegerField()
    receive_list = models.CharField(max_length=100)
    extra_data = models.CharField(max_length=500)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mail_user'


class TaskBaseConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    config_key = models.CharField(max_length=100)
    config_value = models.CharField(max_length=100)
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    extra_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_base_config'


class TaskConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    type = models.IntegerField()
    prize = models.CharField(max_length=5000)
    crontab = models.CharField(max_length=500)
    action = models.CharField(max_length=100)
    check_obj = models.CharField(max_length=500)
    target = models.CharField(max_length=500)
    before_id = models.CharField(max_length=100)
    after_id = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    expired_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    extra_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_config'


class TaskDailyConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.IntegerField()
    rate = models.IntegerField()
    type = models.IntegerField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    extra_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_daily_config'


class TaskRoleInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.CharField(max_length=50)
    task_id = models.CharField(max_length=100)
    type = models.IntegerField()
    prize = models.CharField(max_length=500)
    action = models.CharField(max_length=500)
    check_obj = models.CharField(max_length=500)
    target = models.CharField(max_length=500)
    value = models.CharField(max_length=500)
    status = models.IntegerField()
    start_time = models.DateTimeField()
    expired_time = models.DateTimeField()
    delete_flag = models.IntegerField()
    raw_add_time = models.DateTimeField()
    raw_update_time = models.DateTimeField()
    extra_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'task_role_info'
