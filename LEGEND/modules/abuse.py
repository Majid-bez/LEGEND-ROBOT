import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from LEGEND import dispatcher
from LEGEND.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Jaa na Bsdk, gaand mara jaake.",
    "Tu paidaishi chutiya hai ki koi course kiya hai? ",
    "Mai jaana chahti tum apni gaand kitne mai doge",
    "The world would have been so smooth if your dad had just pulled out",
    "Lund hoti khadi nahi baate kare badi badi",
    "Bas jara apne dono pair failao fir dekho chamatkar?",
    "Jaa na Gandu",
    "Aand ka na Gaand ka, Gyaan jhaare pure Brahmand ka",
    "Dhaat teri maa ki ch*t",
    "Gaand se tatti nikalke jaadugar samajhta hai apne aap ko?",
    "Yeh tera baap ka group nahi hai ja jaake graad marwa'",
    "Please fuck off bitch, and get a life",
    "Tu aise nhi maanega - Mat maan, maa chuda",
    "Tujhse zada sundar teri jali hui gaand hai",
    "Ye aapki Randikhana nhi hai, kripya yaha se dur rahe",
    "Gaad ki shakal ke.",
    "bsdkeee jyada na bol rha he",
    "saale gand marwa apni"
  )
