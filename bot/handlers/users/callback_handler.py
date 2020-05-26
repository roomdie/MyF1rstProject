async def callback_handler(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == "add_channel":
        await callback_query.message.answer(
            "Please write your channel id:"
        )
        await callback_query.answer(text="")
        await ChannelId.id.set()
    elif callback_query.data == "yes_delete_channel":
        delete_channel(user_id, username_user, username_bot)
        await message.answer(
            "Channel deleted."
        )
        await callback_query.answer(text="")
        await state.finish()

    elif callback_query.data == "cancel_delete_bot":
        await message.answer(
            "Cancel."
        )
        await callback_query.answer(text="")
        await state.finish()
    elif callback_query.data == "delete_bot":
        rows = channel_db.select_all()
        for i in rows:
            if username_bot in i:
                markup_delete = types.InlineKeyboardMarkup()
                button_yes = types.InlineKeyboardButton(text="Yes", callback_data="delete_bot_real_1")
                button_no = types.InlineKeyboardButton(text="No", callback_data="about_channel")
                markup_delete.insert(button_yes)
                markup_delete.insert(button_no)
                await callback_query.message.answer(
                    "Delete your Channel?", reply_markup=markup_delete
                )
                await callback_query.answer(text="")