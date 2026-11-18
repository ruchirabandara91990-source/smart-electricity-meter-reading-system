# Smart Electricity Meter Reading System ⚡

> **Developer:** H. M. Ruchira Kanishka Bandara | **Status:** ✅ **COMPLETED**

---

## ⚡ Quick Snapshot (At a Glance)
The **Smart Electricity Meter Reading System** is an innovative IoT-based dual-unit solution designed to solve critical field safety issues (such as pet dog attacks) and operational inefficiencies in the electrical industry. It allows meter readers to inspect kilowatt-hour meters and issue bills directly from outside the front gate without entering the property.

---

## 🛑 1. The Problem & Industry Challenge
Meter readers face severe safety and operational challenges during routine home inspections:
* **Field Safety Risks:** Approximately 5 to 10 meter readers face difficulties and dog-bite hazards every month due to pets[cite: 3].
* **Locked Premises:** Blocked access when occupants are away from home[cite: 3].
* **Hidden Meters:** Rear-wall meter installations force readers to take long detours, wasting valuable time[cite: 3].

---

## ⚙️ 2. Developed Product Architecture (Dual-Unit System)
The product operates in two main interconnected parts:
* **Unit 01 (Indoor / Meter Side):** Installed on the wall directly facing the electricity meter using an articulated metal arm. Powered by standard AC mains with an integrated backup battery[cite: 3, 7].
* **Unit 02 (Outdoor / Gate Side):** Installed inside a protective weatherproof metal box at the front gate or fence[cite: 3, 7]. It features a **3.7-inch LCD Display driven by a Raspberry Pi board**[cite: 3, 7].
* **Communication:** An **ESP32-CAM** mounted at the meter streams live video over a local Wi-Fi network directly to the gate-side display, allowing instant meter verification with zero delay up to 50 meters[cite: 3, 4, 7].
* **Power Supply:** The outdoor unit operates independently using an **18.5V solar panel** and a **PWM solar regulator** charging a **12V 5000mAh battery**, ensuring months of continuous operation[cite: 3, 4, 7].

---

## 🧪 3. Experiments & Testing Iterations
* **Test 01 (Failed):** Used a gate QR code, requiring the meter reader's phone to join the home’s local Wi-Fi network[cite: 4, 8].
* **Test 02 (Failed):** Used an ngrok port-forwarding URL, but it required cumbersome monthly manual reconfigurations[cite: 4, 8].
* **Test 03 (Successful):** Eliminated phones and URLs entirely by linking the ESP32-CAM directly to a dedicated gate-side LCD display for a reliable, standalone live feed[cite: 4, 8].

---

## 🛠️ 4. Used Materials & Components
* **Fabrication Tools:** Welding machine, grinder machine, rivet gun, saw, screwdrivers[cite: 5, 8].
* **Structural Resources:** 30mm box bars, metal angle brackets, iron bars, hard board[cite: 5, 8].
* **Electronic Components:** Raspberry Pi, ESP32-CAM Development Board, 5-inch LCD HDMI/USB Touch Screen, 20W Polycrystalline Solar Panel, 30A Solar Charge Controller (12V/24V), 2.4G Wi-Fi Male Antenna[cite: 5, 8].

---

## 🚀 5. Future Enhancements & Reflections
* **Long-Range Wired Option:** Developing a wired connection alternative to bypass the 20m–30m local Wi-Fi barrier for large properties[cite: 6, 8].
* **Centralized CEB Cloud Network:** Transitioning to public network integration so regional Ceylon Electricity Board (CEB) offices can remotely monitor meters and issue bills directly[cite: 6, 8].
* **Mass Affordability:** Optimizing the design for low-cost mass production so any household can afford it[cite: 6, 8].

---

## 👨‍💻 Developer
* **H. M. Ruchira Kanishka Bandara**[cite: 3]
