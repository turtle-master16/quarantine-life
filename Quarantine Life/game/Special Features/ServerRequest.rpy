init:
    define persistent.server_ending_records = {}
    define persistent.traversed_endings = []
    define persistent.user_device_id = ""
    define persistent.last_server_fetch_date = ""

    define persistent.is_last_online_fetch_failed = False
    define persistent.is_last_online_save_failed = False

init python:
    import requests
    import json
    import uuid
    from datetime import date

    access_url = "https://api.jsonbin.io/v3/b/61a0951f62ed886f9154e4a5"
    master_key = "$2b$10$zxcdZxYcJjoiLzjPPRQKDeBNULrV4/P1Y.J4XRHdn2MGPEkpBvA6u"

    def getJSONBin():
        url = access_url + "/latest"
        headers = {
            "X-Master-Key": master_key,
            "X-Bin-Meta": "false"
        }

        req = requests.get(url, json=None, headers=headers, timeout=15.0)
        return req.text

    def updateTraversedEndingRecords():
        renpy.show_screen("saveEndingRecordScreen")
        renpy.pause(3.0, hard="True")
        try:
            url = access_url
            headers = {
                "Content-Type": "application/json",
                "X-Master-Key": master_key
            }

            jsonBin = json.loads(getJSONBin().encode("ascii","ignore"))
            for index, record in enumerate(jsonBin["server_ending_records"]):
                if record["user_device_id"] == persistent.user_device_id:
                    if record["traversed_endings"] == persistent.server_ending_records:
                        return
                    jsonBin["server_ending_records"].pop(index)
                    jsonBin["server_ending_records"].append({
                        "user_device_id": persistent.user_device_id,
                        "traversed_endings": persistent.traversed_endings
                    })
                    break

            else:
                jsonBin["server_ending_records"].append({
                    "user_device_id": persistent.user_device_id,
                    "traversed_endings": persistent.traversed_endings
                })

            persistent.server_ending_records = jsonBin
            req = requests.put(url, json=jsonBin, headers=headers, timeout=15.0)

        except Exception as exception:
            renpy.hide_screen("saveEndingRecordScreen")
            renpy.show_screen("failedSaveEndingRecordScreen")

            persistent.is_last_online_save_failed = True
            print(exception)
            renpy.pause(3.0, hard="True")

        finally:
            renpy.hide_screen("saveEndingRecordScreen")
            renpy.hide_screen("failedSaveEndingRecordScreen")

    if not persistent.user_device_id:
        persistent.user_device_id = str(uuid.getnode())
        print("yo")


    def getLatestTraversedEndingRecords():
        try:
            if persistent.is_last_online_fetch_failed:
                persistent.is_last_online_fetch_failed = False
            elif persistent.last_server_fetch_date == date.today().strftime("%B %d, %Y"):
                return

            renpy.show_screen("fetchEndingRecordScreen")
            persistent.server_ending_records = json.loads(getJSONBin().encode("ascii","ignore"))
            persistent.last_server_fetch_date = date.today().strftime("%B %d, %Y")

            renpy.pause(3.0, hard="True")

        except Exception as exception:
            renpy.hide_screen("fetchEndingRecordScreen")
            renpy.show_screen("failedFetchEndingRecordScreen")

            persistent.is_last_online_fetch_failed = True
            print(exception)
            renpy.pause(3.0, hard="True")

        finally:
            renpy.hide_screen("fetchEndingRecordScreen")
            renpy.hide_screen("failedFetchEndingRecordScreen")

    def saveLatestTraversedEndingRecords():
        if ending_name not in persistent.traversed_endings:
            persistent.traversed_endings.append(ending_name)
            updateTraversedEndingRecords()
            return

        if persistent.is_last_online_save_failed:
            persistent.is_last_online_save_failed = False
            updateTraversedEndingRecords()
            return

    def getEndingTraversePercentage(ending_name, reverse=False):
        if not persistent.server_ending_records:
            return "0%"

        number_of_ending_traversed = 0
        for index, record in enumerate(persistent.server_ending_records["server_ending_records"]):
            if record["user_device_id"] == persistent.user_device_id:
                continue

            if ending_name == "quarantine violator" and reverse:
                if ending_name in record["traversed_endings"] and len(record["traversed_endings"]) == 1:
                    number_of_ending_traversed += 1
                    continue

            if ending_name == "safety is priority" and reverse:
                if ending_name in record["traversed_endings"] and len(record["traversed_endings"]) == 1:
                    number_of_ending_traversed += 1
                    continue

                if set([ending_name in record["traversed_endings"], "quarantine violator"]).issubset(record["traversed_endings"]) and len(record["traversed_endings"]) == 2:
                    number_of_ending_traversed += 1
                    continue

            for current_ending in record["traversed_endings"]:
                if current_ending == ending_name:
                    number_of_ending_traversed += 1

        print(len(persistent.server_ending_records["server_ending_records"]))
        print(persistent.server_ending_records["server_ending_records"])
        print(str(number_of_ending_traversed) + " endings")
        print(number_of_ending_traversed / len(persistent.server_ending_records["server_ending_records"]))

        if reverse:
            return str((float(len(persistent.server_ending_records["server_ending_records"]) - number_of_ending_traversed) / len(persistent.server_ending_records["server_ending_records"])) * 100) + "%"
        return str((float(number_of_ending_traversed) / len(persistent.server_ending_records["server_ending_records"])) * 100) + "%"

screen fetchEndingRecordScreen:
    zorder 100
    add Solid("#EEA900DD")

    vbox at show_ending_screen:
        xalign 0.5
        yalign 0.5

        text "Fetching choices online...":
            xalign 0.5
            yalign 0.5
            color "#fff"
            size 70

        text "Please don't turn off the game.":
            xalign 0.5
            yalign 0.6
            color "#fff"
            size 40

screen failedFetchEndingRecordScreen:
    zorder 100
    add Solid("#F9502EDD")

    vbox at show_ending_screen:
        xalign 0.5
        yalign 0.5

        text "Failed to fetch choices online...":
            xalign 0.5
            yalign 0.5
            color "#fff"
            size 70

        text "Please connect your device to the internet.":
            xalign 0.5
            yalign 0.6
            color "#fff"
            size 40

screen saveEndingRecordScreen:
    zorder 100
    add Solid("#17BE7288")

    vbox at show_ending_screen:
        xalign 0.5
        yalign 0.5

        text "Saving your choices online...":
            xalign 0.5
            yalign 0.5
            color "#fff"
            size 70

        text "Please don't turn off the game.":
            xalign 0.5
            yalign 0.6
            color "#fff"
            size 40

screen failedSaveEndingRecordScreen:
    zorder 100
    add Solid("#F9502E88")

    vbox at show_ending_screen:
        xalign 0.5
        yalign 0.5

        text "Failed to save your choices online...":
            xalign 0.5
            yalign 0.5
            color "#fff"
            size 70

        text "Please connect your device to the internet.":
            xalign 0.5
            yalign 0.6
            color "#fff"
            size 40

transform show_ending_screen:
    on show:
        alpha .0
        linear 2.0 alpha 1.0

    on hide:
        alpha .0
