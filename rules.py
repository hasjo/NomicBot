base_rules = {
        "101": { "text": "All players must always abide by all the rules then in effect, in the form in which they are then in effect. The rules in the Initial Set are in effect whenever a game begins. The Initial Set consists of Rules 101-116 (immutable) and 201-213 (mutable).",
                 "mutable": False,
                },
        "102": { "text": "Initially rules in the 100's are immutable and rules in the 200's are mutable. Rules subsequently enacted or transmuted (that is, changed from immutable to mutable or vice versa) may be immutable or mutable regardless of their numbers, and rules in the Initial Set may be transmuted regardless of their numbers.",
                 "mutable": False,
                },
        "103": { "text": "A rule-change is any of the following: (1) the enactment, repeal, or amendment of a mutable rule; (2) the enactment, repeal, or amendment of an amendment of a mutable rule; or (3) the transmutation of an immutable rule into a mutable rule or vice versa.",
                 "mutable": False,
                },
        "104": { "text": "All rule-changes proposed in the proper way shall be voted on. They will be adopted if and only if they receive the required number of votes.",
                 "mutable": False,
                },
        "105": { "text": "Every player is an eligible voter. Every eligible voter must participate in every vote on rule-changes.",
                 "mutable": False,
                },
        "106": { "text": "All proposed rule-changes shall be written down before they are voted on. If they are adopted, they shall guide play in the form in which they were voted on.",
                 "mutable": False,
                },
        "107": { "text": "No rule-change may take effect earlier than the moment of the completion of the vote that adopted it, even if its wording explicitly states otherwise. No rule-change may have retroactive application.",
                 "mutable": False,
                },
        "108": { "text": "Each proposed rule-change shall be given a number for reference. The numbers shall begin with 301, and each rule-change proposed in the proper way shall receive the next successive integer, whether or not the proposal is adopted. If a rule is repealed and reenacted, it receives the number of the proposal to reenact it. If a rule is amended or transmuted, it receives the number of the proposal to amend or transmute it. If an amendment is amended or repealed, the entire rule of which it is a part receives the number of the proposal to amend or repeal the amendment.",
                 "mutable": False,
                },
        "109": { "text": "Rule-changes that transmute immutable rules into mutable rules may be adopted if and only if the vote is unanimous among the eligible voters. Transmutation shall not be implied, but must be stated explicitly in a proposal to take effect.",
                 "mutable": False,
                },
        "110": { "text": "In a conflict between a mutable and an immutable rule, the immutable rule takes precedence and the mutable rule shall be entirely void. For the purposes of this rule a proposal to transmute an immutable rule does not \"conflict\" with that immutable rule.",
                 "mutable": False,
                },
        "111": { "text": " If a rule-change as proposed is unclear, ambiguous, paradoxical, or destructive of play, or if it arguably consists of two or more rule-changes compounded or is an amendment that makes no difference, or if it is otherwise of questionable value, then the other players may suggest amendments or argue against the proposal before the vote. A reasonable time must be allowed for this debate. The proponent decides the final form in which the proposal is to be voted on and, unless the Judge has been asked to do so, also decides the time to end debate and vote.",
                 "mutable": False,
                },
        "112": { "text": "The state of affairs that constitutes winning may not be altered from achieving n points to any other state of affairs. The magnitude of n and the means of earning points may be changed, and rules that establish a winner when play cannot continue may be enacted and (while they are mutable) be amended or repealed.",
                 "mutable": False,
                },
        "113": { "text": "A player always has the option to forfeit the game rather than continue to play or incur a game penalty. No penalty worse than losing, in the judgment of the player to incur it, may be imposed.",
                 "mutable": False,
                },
        "114": { "text": "There must always be at least one mutable rule. The adoption of rule-changes must never become completely impermissible.",
                 "mutable": False,
                },
        "115": { "text": "Rule-changes that affect rules needed to allow or apply rule-changes are as permissible as other rule-changes. Even rule-changes that amend or repeal their own authority are permissible. No rule-change or type of move is impermissible solely on account of the self-reference or self-application of a rule.",
                 "mutable": False,
                },
        "116": { "text": "Whatever is not prohibited or regulated by a rule is permitted and unregulated, with the sole exception of changing the rules, which is permitted only when a rule or set of rules explicitly or implicitly permits it.",
                 "mutable": False,
                },
        "201": { "text": "Players shall alternate in clockwise order, taking one whole turn apiece. Turns may not be skipped or passed, and parts of turns may not be omitted. All players begin with zero points. In mail and computer games, players shall alternate by player number.",
                 "mutable": True,
                },
        "202": { "text": "One turn consists of two parts in this order: (1) proposing one rule-change and having it voted on, and (2) throwing one die once and adding the number of points on its face to one's score. In mail and computer games, instead of throwing a die, players subtract 291 from the ordinal number of their proposal and multiply the result by the fraction of favorable votes it received, rounded to the nearest integer. (This yields a number between 0 and 10 for the first player, with the upper limit increasing by one each turn; more points are awarded for more popular proposals.)",
                 "mutable": True,
                },
        "203": { "text": "A rule-change is adopted if and only if the vote is unanimous among the eligible voters. If this rule is not amended by the end of the second complete circuit of turns, it automatically changes to require only a simple majority.",
                 "mutable": True,
                },
        "204": { "text": "If and when rule-changes can be adopted without unanimity, the players who vote against winning proposals shall receive 10 points each.",
                 "mutable": True,
                },
        "205": { "text": "An adopted rule-change takes full effect at the moment of the completion of the vote that adopted it.",
                 "mutable": True,
                },
        "206": { "text": "When a proposed rule-change is defeated, the player who proposed it loses 10 points.",
                 "mutable": True,
                },
        "207": { "text": "Each player always has exactly one vote.",
                 "mutable": True,
                },
        "208": { "text": "The winner is the first player to achieve 100 (positive) points.",
                 "mutable": True,
                },
        "209": { "text": "At no time may there be more than 25 mutable rules.",
                 "mutable": True,
                },
        "210": { "text": "Players may not conspire or consult on the making of future rule-changes unless they are team-mates. The first paragraph of this rule does not apply to games by mail or computer.",
                 "mutable": True,
                },
        "211": { "text": "If two or more mutable rules conflict with one another, or if two or more immutable rules conflict with one another, then the rule with the lowest ordinal number takes precedence. If at least one of the rules in conflict explicitly says of itself that it defers to another rule (or type of rule) or takes precedence over another rule (or type of rule), then such provisions shall supersede the numerical method for determining precedence. If two or more rules claim to take precedence over one another or to defer to one another, then the numerical method again governs.",
                 "mutable": True,
                },
        "212-1": { "text": "If players disagree about the legality of a move or the interpretation or application of a rule, then the player preceding the one moving is to be the Judge and decide the question. Disagreement for the purposes of this rule may be created by the insistence of any player. This process is called invoking Judgment. When Judgment has been invoked, the next player may not begin his or her turn without the consent of a majority of the other players. The Judge's Judgment may be overruled only by a unanimous vote of the other players taken before the next turn is begun. If a Judge's Judgment is overruled, then the player preceding the Judge in the playing order becomes the new Judge for the question, and so on, except that no player is to be Judge during his or her own turn or during the turn of a team-mate.",
                 "mutable": True
                },
        "212-2": { "text": "Unless a Judge is overruled, one Judge settles all questions arising from the game until the next turn is begun, including questions as to his or her own legitimacy and jurisdiction as Judge. New Judges are not bound by the decisions of old Judges. New Judges may, however, settle only those questions on which the players currently disagree and that affect the completion of the turn in which Judgment was invoked. All decisions by Judges shall be in accordance with all the rules then in effect; but when the rules are silent, inconsistent, or unclear on the point at issue, then the Judge shall consider game-custom and the spirit of the game before applying other standards.",
                 "mutable": True,
                },
        "213": { "text": "If the rules are changed so that further play is impossible, or if the legality of a move cannot be determined with finality, or if by the Judge's best reasoning, not overruled, a move appears equally legal and illegal, then the first player unable to complete a turn is the winner. This rule takes precedence over every other rule determining the winner.",
                 "mutable": True,
                },
}
